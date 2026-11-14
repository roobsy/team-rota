"""Request plumbing (ADU-02): the caller resolved once per request through MemberDirectory, one session per
request shared by every service of the request, and the Problem refusal shape of the cross-cutting rules."""

from __future__ import annotations

from collections.abc import AsyncIterator

from fastapi import Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app import db
from app.ports import Caller

bearer = HTTPBearer(auto_error=False, scheme_name="bearer")


class ProblemError(Exception):
    """A refusal: {reason, detail, ...}; the status follows the bucket of the Reason codes table."""

    def __init__(self, status: int, reason: str, title: str, detail: str, **extra: object) -> None:
        super().__init__(reason)
        self.status, self.reason, self.title, self.detail, self.extra = status, reason, title, detail, extra


def problem_response(status: int, reason: str, title: str, detail: str, **extra: object) -> JSONResponse:
    return JSONResponse(
        {"type": "about:blank", "title": title, "detail": detail, "reason": reason, **extra}, status
    )


async def get_session(request: Request) -> AsyncIterator[Session]:
    """The request's one session (D-14), current (db.use_session) for the whole request. FastAPI caches the
    dependency, so every dependent of the request shares it. It is async because a ContextVar set in a sync
    dependency is not visible to the endpoint. On the way out the previous current session is restored and
    this one closed, which rolls back what was not committed. It never commits: the API layer commits a write
    before it answers, because this exit runs after the response is sent."""
    session = db.session_for(engine_of(request))
    try:
        with db.use_session(session):
            yield session
    finally:
        session.close()


def require_caller(
    request: Request,
    creds: HTTPAuthorizationCredentials | None = Depends(bearer),
    _session: Session = Depends(get_session),
) -> Caller:
    """unauthenticated before anything else: no token, an unknown token or an inactive member's token
    (R-identity-06). It depends on the request's session, so caller_for_token reads it (D-14)."""
    token = creds.credentials if creds else None
    caller = request.app.state.ports.member_directory.caller_for_token(token) if token else None
    if caller is None:
        raise ProblemError(401, "unauthenticated", "Not signed in", "Sign in first.")
    return caller


def engine_of(request: Request):
    app = request.app
    if app.state.engine is None:
        app.state.engine = db.engine_for(app.state.workspace)
    return app.state.engine
