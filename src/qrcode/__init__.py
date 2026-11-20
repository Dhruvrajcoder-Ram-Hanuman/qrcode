import argparse
import base64
from io import BytesIO
from pathlib import Path
import segno
import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time
app = FastAPI(title="QR Code Generator")

app.mount("/static", StaticFiles(directory='static'), name="static")

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="item.html")


@app.post("/code")#, response_class=HTMLResponse)
async def generate_code(request: Request, data: str = Form(...)) -> HTMLResponse:
    if('@' in data and data.endswith(".com") and not data.startswith("@")):
        print(data)
        qr = segno.make(data, error="M", micro=False, boost_error=False)
        qr.save('static/qrcode.png')
        t=time.time()
        qr.save(f'qr//{t}.png')
        return templates.TemplateResponse(
            request=request,
            name="data.html",
            context={"data": data},
        )
    else:
        return {"error": "Invalid email address"}

def run() -> None:
    parser = argparse.ArgumentParser(description="Run the QR Code Generator web application.")
    parser.add_argument("command", nargs="?", choices=("dev",), help="Run in dev mode with live reloading")
    parser.add_argument("--host", default="127.0.0.1", help="Host address to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind (default: 8000)")
    args = parser.parse_args()

    uvicorn.run(
        "qrcode:app",
        host=args.host,
        port=args.port,
        reload=args.command == "dev",
    )
