from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
import os, httpx

permlinks = ['/']
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/js", StaticFiles(directory="static/js"), name="bundles")
app.mount("/images", StaticFiles(directory="static/images"), name="images")
app.mount("/flags", StaticFiles(directory="static/flags"), name="flags")
app.mount("/fonts", StaticFiles(directory="static/fonts"), name="fonts")
app.mount("/icons", StaticFiles(directory="static/icons"), name="icons")
app.mount("/lang", StaticFiles(directory="static/lang"), name="languages")
app.mount("/maps", StaticFiles(directory="static/maps"), name="maps")
app.mount("/sprites", StaticFiles(directory="static/sprites"), name="sprites")

app.mount("/mods", StaticFiles(directory="mods"), name="mods")


@app.get("/")
async def root():
    return FileResponse("static/index.html", media_type="text/html")

@app.get("/api/env")
async def env():
    return {"game_env": "prod"}
