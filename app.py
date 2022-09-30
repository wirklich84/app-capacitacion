from fastapi import FastAPI, Request
from database import iniciar_db
from routes.users import router_users as UserRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def start_database():
    await iniciar_db()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('login.html', context={"request" : request})

app.include_router(UserRouter, tags=["User"], prefix="/user")