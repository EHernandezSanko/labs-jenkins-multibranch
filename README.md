# Simple FastAPI

A minimal FastAPI application with versioned health and home endpoints.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Endpoints

- `GET /v1/health` returns the API status, version, and branch as JSON. The
  branch is read from `APP_BRANCH`, `GITHUB_REF_NAME`, or `BRANCH_NAME`, in that
  order; if none is set, the app detects the checked-out Git branch.
- `GET /v1/home` returns a simple HTML page.
- `GET /docs` opens the interactive API documentation.
