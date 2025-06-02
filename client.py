from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
import os, http.client, json

def rget(domain):
    parts = domain.split('/', 1)
    host = parts[0]
    path = '/' + parts[1] if len(parts) > 1 else '/'
    
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path)
    response = conn.getresponse()
    data = response.read().decode()
    conn.close()
    
    return json.loads(data)

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

@app.get("/api/public_lobbies")
async def multiplayer():
    return rget('openfront.io/api/public_lobbies')
