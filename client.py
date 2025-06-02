from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
import os, httpx

permlinks = ['/']
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/js", StaticFiles(directory="static/js"), name="bundles")
app.mount("/images", StaticFiles(directory="static/images"), name="images")
app.mount("/mods", StaticFiles(directory="mods"), name="mods")

@app.get("/")
async def root():
    return FileResponse("static/index.html", media_type="text/html")

@app.get("/api/env")
async def env():
    return {"game_env": "prod"}
