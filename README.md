# QR Code Generator

A modern, fast web application for generating QR codes built with **FastAPI**, **Segno**, and **Jinja2**, managed by **uv**.

---

## Features

- **Instant QR Generation**: Encode text, URLs, contact info, and more using high-quality Segno encoding.
- **Modern Responsive UI**: Clean, mobile-friendly interface for generating and downloading QR codes.
- **Fast & Lightweight**: Built on top of FastAPI and Uvicorn.
- **Direct Download**: One-click PNG download for generated QR codes.

---

## Installing `uv` (if not already installed)

`uv` is an extremely fast Python package and project manager written in Rust.

### On Windows:
You can install `uv` via **WinGet**:
```powershell
winget install --id=astral-sh.uv -e
```
Or via the official standalone installer in PowerShell:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:
```powershell
uv --version
```

---

## Running the Application

`uv` automatically handles creating the virtual environment, syncing dependencies, and running the project.

### 1. Run the Server
From the project root folder:
```powershell
uv run main
```
Or:
```powershell
uv run qrcode
```
Or directly with Python:
```powershell
uv run python main.py
```

### 2. Run in Development Mode (Live Reloading)
To enable automatic reload on file changes:
```powershell
uv run main dev
```

### 3. Custom Host & Port
```powershell
uv run main --host 0.0.0.0 --port 8080
```

Once running, open your browser and navigate to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)
