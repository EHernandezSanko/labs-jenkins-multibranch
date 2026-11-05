import os
import subprocess

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

API_VERSION = "1.0.0"


def _get_branch_name() -> str:
    for variable in ("APP_BRANCH", "GITHUB_REF_NAME", "BRANCH_NAME"):
        branch = os.getenv(variable)
        if branch:
            return branch

    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            check=True,
            capture_output=True,
            text=True,
            timeout=1,
        )
    except (OSError, subprocess.SubprocessError):
        return "unknown"

    return result.stdout.strip() or "unknown"


BRANCH_NAME = _get_branch_name()
app = FastAPI(title="Simple API", version=API_VERSION)


@app.get("/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": API_VERSION, "branch": BRANCH_NAME}


@app.get("/v1/home", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Home</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p>The API is running.</p>
  </body>
</html>"""
