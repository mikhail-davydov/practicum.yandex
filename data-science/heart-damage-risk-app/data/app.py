import pickle

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles


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
