"""The database: one SQLite file per workspace path, created on first use; never a shared in-memory engine."""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from app.models import Base

FILE_NAME = "rota.sqlite"


def engine_for(workspace: Path) -> Engine:
    """An engine on <workspace>/rota.sqlite; folder and tables are created if absent (pathlib only)."""
    workspace = Path(workspace)
    workspace.mkdir(parents=True, exist_ok=True)
    engine = create_engine(f"sqlite:///{(workspace / FILE_NAME).as_posix()}", future=True)

    @event.listens_for(engine, "connect")
    def _foreign_keys(dbapi_connection, _record) -> None:  # SQLite enforces foreign keys only when asked
        dbapi_connection.execute("PRAGMA foreign_keys=ON")

    Base.metadata.create_all(engine)
    return engine


def session_for(engine: Engine) -> Session:
    """One session per request (the API layer opens it; every service of the request shares it)."""
    return sessionmaker(bind=engine, future=True, expire_on_commit=False)()
