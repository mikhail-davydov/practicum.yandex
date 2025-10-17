import pickle

import pandas as pd
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Шаблоны Jinja2 для рендеринга HTML-шаблонов
templates = Jinja2Templates(directory="templates")


def create_app(test_config=None):
    is_test = True if (test_config and test_config.get('TESTING', False) == True) else False

    app = FastAPI()

    if not is_test:
        # Монтируем папку static для обработки статики
        app.mount("/static", StaticFiles(directory="static"), name="static")

    # Загрузим обученную модель
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    return app, model


app, model = create_app()


def fill_na_with_median(df: pd.DataFrame):
    """
    Найдет все колонки датасета, содержащие пустые значения (NaN), и заполнит их медианой каждой колонки.

    Parameters:
    -----------
    df: pandas.DataFrame
        Входной датасет.

    Returns:
    --------
    filled_df: pandas.DataFrame
        Датасет с заполненными пустыми значениями.
    """
    # Сначала найдем все колонки, содержащие NaN
    nan_columns = df.columns[df.isnull().any()]

    # Для каждой колонки с пустыми значениями заполним их медианой
    for col in nan_columns:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

    return df


def prepare_data(df: pd.DataFrame):
    """
    Подготовит датасет к использованию с обученной моделью

    Parameters:
    -----------
    df: pandas.DataFrame
        Входной датасет.

    Returns:
    --------
    filled_df: pandas.DataFrame
        Подготовленный датасет.
    """
    # Переименуем столбцы
    df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

    # Заполним пропуски
    df = fill_na_with_median(df)

    # Поменяем значения для признака gender
    df.loc[df['gender'] == 'Male', 'gender'] = '1.0'
    df.loc[df['gender'] == 'Female', 'gender'] = '0.0'

    return df


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

        return df_prepared['prediction_proba'].sample(10).to_json(orient='index')
    except Exception as e:
        return {"error": f"Ошибка при обработке датасета: {e}"}


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
