# Simple FastAPI

A minimal FastAPI application with versioned health and home endpoints.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Run with Docker

Build the image and start the API:

```powershell
docker build -t simple-fastapi .
docker run --rm -p 8000:8000 simple-fastapi
```

The API is available at `http://localhost:8000`. To report a branch in the
health response from inside the container, pass it with `APP_BRANCH`:

```powershell
docker run --rm -p 8000:8000 -e APP_BRANCH=dev simple-fastapi
```

## Endpoints

- `GET /v1/health` returns the API status, version, and branch as JSON. The
  branch is read from `APP_BRANCH`, `GITHUB_REF_NAME`, or `BRANCH_NAME`, in that
  order; if none is set, the app detects the checked-out Git branch.
- `GET /v1/home` returns a simple HTML page.
- `GET /docs` opens the interactive API documentation.
