#!/usr/bin/env python3
"""The layering ratchet, stdlib only (copied into tests/layering_scan.py by phase 5).

Reads tests/layering.json:
  { "package_root": "src", "package": "app",
    "layers": { "model": ["app.models", "app.db"], "core": ["app.core.*", "app.*.service"],
                "api": ["app.api.*"], "root": ["app.cli", "app.main"] },
    "forbidden": [["core", "api"], ["core", "root"], ["model", "core"], ["model", "api"], ["api", "root"]],
    "frozen": [["core", "model"]] }
Walks the package, parses every import with `ast`, resolves importer and target to layers by fnmatch, and
produces edges keyed (kind, importer, target, placement, symbol): kind "forbidden" (a crossing the config
forbids - asserted zero, never written to the baseline), "frozen" (a tolerated crossing or a private reach -
frozen in the baseline, may only shrink). The baseline is compared both ways: a new edge fails, a vanished
edge fails (regenerate on purpose).

usage: layering_scan.py [--config tests/layering.json] [--baseline tests/layering_baseline.json]
                        [--write-baseline] [--json]
exit 0 = clean; 1 = findings (printed, one per line).
Output is ASCII-only on purpose: it must print on a cp1252 Windows console (plugin FB-18).
"""

from __future__ import annotations

import argparse
import ast
import fnmatch
import json
import sys
from pathlib import Path

REGENERATE = "python tests/layering_scan.py --write-baseline"


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def module_name(file: Path, package_root: Path) -> str:
    rel = file.relative_to(package_root).with_suffix("")
    parts = list(rel.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def layer_of(module: str, layers: dict[str, list[str]]) -> str | None:
    for name, patterns in layers.items():
        for p in patterns:
            family = p[:-2] if p.endswith(".*") else None  # "app.api.*" also names the package app.api itself
            if (
                fnmatch.fnmatchcase(module, p)
                or module == p
                or module.startswith(p + ".")
                or (family and (module == family or module.startswith(family + ".")))
            ):
                return name
    return None


def _imports(tree: ast.AST):
    """Yield (node, placement) for every import, placement 'function' when inside a def, else 'module'."""

    def walk(node: ast.AST, in_function: bool):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.Import, ast.ImportFrom)):
                yield child, ("function" if in_function else "module")
            yield from walk(child, in_function or isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)))

    yield from walk(tree, False)


def scan(cfg: dict, root: Path) -> tuple[list[dict], set[str]]:
    package_root = root / cfg.get("package_root", "src")
    pkg = cfg["package"]
    pkg_dir = package_root / pkg
    layers = cfg.get("layers", {})
    forbidden = {tuple(x) for x in cfg.get("forbidden", [])}
    frozen = {tuple(x) for x in cfg.get("frozen", [])}
    edges: list[dict] = []
    modules: set[str] = set()
    for file in sorted(pkg_dir.rglob("*.py")):
        importer = module_name(file, package_root)
        modules.add(importer)
        tree = ast.parse(file.read_text(encoding="utf-8"), filename=str(file))
        for node, placement in _imports(tree):
            targets: list[tuple[str, str]] = []
            if isinstance(node, ast.Import):
                for a in node.names:
                    targets.append((a.name, ""))
            else:
                base = node.module or ""
                if node.level:
                    base = ".".join(importer.split(".")[: -node.level] + ([base] if base else []))
                for a in node.names:
                    targets.append((base, a.name))
            for target, symbol in targets:
                if not (target == pkg or target.startswith(pkg + ".")):
                    continue
                if target == importer:
                    continue
                li, lt = layer_of(importer, layers), layer_of(target, layers)
                private = symbol.startswith("_")
                kind = None
                if li and lt and li != lt and (li, lt) in forbidden:
                    kind = "forbidden"
                elif (li and lt and li != lt and (li, lt) in frozen) or private:
                    kind = "frozen"
                if kind:
                    imported = (
                        f"{target}.{symbol}" if symbol else target
                    )  # the name as written, for the message; the key stays (target, private symbol)
                    edges.append(
                        {
                            "kind": kind,
                            "importer": importer,
                            "target": target,
                            "imported": imported,
                            "placement": placement,
                            "symbol": symbol if private else "",
                            "file": str(file.relative_to(root)),
                            "line": node.lineno,
                            "clause": f"{li}->{lt}",
                        }
                    )
    return edges, modules


def key(e: dict) -> tuple:
    return (e["kind"], e["importer"], e["target"], e["placement"], e["symbol"])


def compare(baseline: list[dict], current: list[dict]) -> tuple[list[dict], list[dict]]:
    b = {key(e): e for e in baseline}
    c = {key(e): e for e in current}
    added = [c[k] for k in c if k not in b]
    removed = [b[k] for k in b if k not in c]
    return added, removed


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="tests/layering.json")
    ap.add_argument("--baseline", default="tests/layering_baseline.json")
    ap.add_argument("--root", default=".")
    ap.add_argument("--write-baseline", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    cfg = load_config(root / a.config)
    edges, modules = scan(cfg, root)
    forbidden = [e for e in edges if e["kind"] == "forbidden"]
    frozen = [e for e in edges if e["kind"] == "frozen"]
    if a.json:
        print(json.dumps({"edges": edges, "modules": sorted(modules)}, indent=1))
        return 0
    problems = [
        f"{e['file']}:{e['line']} - {e['importer']} imports {e['imported']} "
        f"({e['clause']}: forbidden by the layering law)"
        for e in forbidden
    ]
    bpath = root / a.baseline
    if a.write_baseline:
        bpath.write_text(
            json.dumps(
                {
                    "note": "frozen edges; regenerate deliberately with: " + REGENERATE,
                    "modules": len(modules),
                    "edges": [
                        {k: e[k] for k in ("kind", "importer", "target", "placement", "symbol")}
                        for e in frozen
                    ],
                },
                indent=1,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"baseline written: {len(frozen)} frozen edge(s), {len(modules)} module(s)")
        # a forbidden crossing is never frozen: the baseline holds only tolerated edges;
        # the next plain run fails on it
        for pr in problems:
            print("not frozen (forbidden, the next run fails on it): " + pr)
        return 0
    elif bpath.exists():
        base = json.loads(bpath.read_text(encoding="utf-8"))
        added, removed = compare(base.get("edges", []), frozen)
        for e in added:
            sym = (" ." + e["symbol"]) if e["symbol"] else ""
            problems.append(
                f"new frozen edge not in the baseline: {e['importer']} -> {e['target']}{sym} "
                f"({e['file']}:{e['line']}) - regenerate deliberately: {REGENERATE}"
            )
        for e in removed:
            sym = (" ." + e["symbol"]) if e["symbol"] else ""
            problems.append(
                f"baseline edge no longer in the code: {e['importer']} -> {e['target']}{sym} "
                f"- the baseline is stale: {REGENERATE}"
            )
        if len(modules) < int(base.get("modules", 0)):
            problems.append(
                f"the walk found {len(modules)} modules, the baseline knew {base['modules']}: "
                "an empty walk passes every other check, so this fails"
            )
    else:
        problems.append(f"no baseline at {a.baseline}: generate it on purpose: {REGENERATE}")
    for p in problems:
        print(p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
