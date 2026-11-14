"""The database: one SQLite file per workspace path, created on first use; never a shared in-memory engine.

The current session (D-14; design/INTERFACES.md, Domain services): every service and port implementation reads
and writes in current_session() and never opens, commits or closes one. A request (deps.get_session), the
operator's command and a test (unit_of_work) make a session current.
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from pathlib import Path

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from app.models import Base

FILE_NAME = "rota.sqlite"

#: the one ContextVar of the current session, private to this module (design/INTERFACES.md, Domain services)
_current: ContextVar[Session | None] = ContextVar("app.db.current_session", default=None)


class NoCurrentSession(RuntimeError):
    """No session is current: the call came from outside a request, the operator's command or a unit of
    work."""


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


def current_session() -> Session:
    """The current session; raises NoCurrentSession when none is (a service never opens one quietly)."""
    session = _current.get()
    if session is None:
        raise NoCurrentSession(
            "no session is current: call inside a request, or inside db.unit_of_work(engine) (D-14)"
        )
    return session


@contextmanager
def use_session(session: Session) -> Iterator[Session]:
    """`session` is current for the block; on exit the previous one is restored with the token this block set,
    so nested blocks and concurrent requests stay apart. It commits nothing and closes nothing."""
    token = _current.set(session)
    try:
        yield session
    finally:
        _current.reset(token)


@contextmanager
def unit_of_work(engine: Engine) -> Iterator[Session]:
    """A new session on `engine`, current for the block: committed when the block returns, rolled back when
    it raises, then closed (the operator's command and the tests; a request uses deps.get_session)."""
    session = session_for(engine)
    try:
        with use_session(session):
            yield session
            session.commit()
    except BaseException:
        session.rollback()
        raise
    finally:
        session.close()
