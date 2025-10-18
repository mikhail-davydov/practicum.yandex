import pandas as pd
from fastapi import Request, UploadFile, File, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from data.app import create_app
from data.function import prepare_data
from log.logger import get_logger

# Создаем экземпляр logger
log = get_logger(__name__)

# Шаблоны Jinja2 для рендеринга HTML-шаблонов
templates = Jinja2Templates(directory="templates")

# Создаем приложение
app, model = create_app()


@app.post("/predict")
async def predict(file: UploadFile = File(...), show_full: bool = Query(True), show_percent: bool = Query(False)):
    try:
        log.info(f"request, show_full: {show_full}, show_percent: {show_percent}")

        csv_buffer = file.file

        df_original = pd.read_csv(csv_buffer, index_col=0)
        df = df_original.copy().set_index("id")

        # Подготовим данные
        pd.set_option("display.float_format", "{:,.2f}".format)
        df_prepared = prepare_data(df)

        # Предсказание с помощью восстановленной модели
        predictions = model.predict(df_prepared.copy())
        predictions_proba = model.predict_proba(df_prepared.copy())[:, 1]

        df_prepared['prediction'] = predictions
        df_prepared['prediction_proba'] = (predictions_proba * 100).round(2)

        df = df_prepared['prediction_proba'] if show_percent else df_prepared['prediction']

        return df.to_json(orient='index') if show_full else df.sample(10).to_json(orient='index')
    except Exception as e:
        log.error(e, exc_info=True)
        return {"error": f"Ошибка при обработке датасета: {e}"}


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
