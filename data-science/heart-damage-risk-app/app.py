import pandas as pd
import requests
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Монтируем папку static для обработки статики
app.mount("/static", StaticFiles(directory="static"), name="static")

# Шаблоны Jinja2 для рендеринга HTML-шаблонов
templates = Jinja2Templates(directory="templates")


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    response = requests.post("https://example.com/predict", json=df.to_dict())

    if response.status_code != 200:
        return {"error": f"Ошибка при обращении к внешнему сервису: {response.text}"}

    return response.json()


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
