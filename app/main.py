from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/tv-shows", response_class=HTMLResponse)
async def tv_shows(request: Request):
    return templates.TemplateResponse("tv_shows.html", {"request": request})

@app.get("/movies", response_class=HTMLResponse)
async def movies(request: Request):
    return templates.TemplateResponse("movies.html", {"request": request})

@app.get("/new-popular", response_class=HTMLResponse)
async def new_popular(request: Request):
    return templates.TemplateResponse("new_popular.html", {"request": request})

@app.get("/my-list", response_class=HTMLResponse)
async def my_list(request: Request):
    return templates.TemplateResponse("my_list.html", {"request": request})
