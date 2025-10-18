import pandas as pd
from fastapi import Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from data.app import create_app
from data.function import prepare_data
from log.logger import get_logger

# Создаем экземпляр logger
log = get_logger(__name__)

# Шаблоны Jinja2 для рендеринга HTML-шаблонов
templates = Jinja2Templates(directory="templates")

app, model = create_app()


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        df_original = pd.read_csv(file.file, index_col=0)
        df = df_original.copy().set_index("id")

        # Подготовим данные
        pd.set_option("display.float_format", "{:,.2f}".format)
        df_prepared = prepare_data(df)

        # Предсказание с помощью восстановленной модели
        predictions = model.predict(df_prepared.copy())
        predictions_proba = model.predict_proba(df_prepared.copy())[:, 1]

        df_prepared['prediction'] = predictions
        df_prepared['prediction_proba'] = (predictions_proba * 100).round(2)

        predictions_proba_df = df_prepared[['prediction', 'prediction_proba']].head().to_json()
        log.info(f"predictions_proba_df no orient: {predictions_proba_df}")

        predictions_proba_df = df_prepared[['prediction', 'prediction_proba']].head().to_json(orient='index')
        log.info(f"predictions_proba_df orient=index: {predictions_proba_df}")

        predictions_proba_df = df_prepared[['prediction', 'prediction_proba']].head().to_json(orient='records')
        log.info(f"predictions_proba_df orient=records: {predictions_proba_df}")

        return df_prepared['prediction_proba'].sample(10).to_json(orient='index')
    except Exception as e:
        return {"error": f"Ошибка при обработке датасета: {e}"}


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
