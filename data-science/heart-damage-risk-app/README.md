# Проект: Приложение для предсказание рисков сердечного приступа

<!-- TOC -->
* [Общая информация и цель проекта](#общая-информация-и-цель-проекта)
* [Задачи проекта](#задачи-проекта)
* [Как запустить приложение](#как-запустить-приложение)
  * [Из исходников](#из-исходников)
  * [В docker](#в-docker)
* [Стек](#стек)
<!-- TOC -->

## Общая информация и цель проекта

В проекте предполагается работа с датасетом из открытого источника. Требуется разработать модель машинного обучения, а также подготовить библиотеку и интерфейс к ней для предсказания на тестовой выборке.


## Задачи проекта

Разработать Fast API приложение для загрузки данынх для предсказаний в формате CSV и получении результатов предсказаний в формате JSON


## Как запустить приложение

Скачать репозиторий с GitHub по ссылке
```bash
curl -X GET https://github.com/mikhail-davydov/practicum.yandex/archive/refs/heads/main.zip -o practicum-yandex.zip
```
Распаковать архив
```bash
unzip practicum-yandex.zip -d practicum-yandex
```
Перейти в директорию с приложением 
```bash
cd practicum-yandex/data-science/heart-damage-risk-app
```


### Из исходников

Должен быть установлен python 3.12.

Создать новое `.venv` окружение в директории `heart-damage-risk-app`
```bash
python -m venv .venv
```
Активировать новое окружение
- Linux
```bash
source .venv/bin/activate
```
- Windows
```
.venv\Scripts\activate.bat
```
Выполнить установку необходимых пакетов из файла `requirements.txt`
```bash
pip install -r requirements.txt
```
Запустить приложение
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
Открыть в браузере ссылку http://localhost:8000/ 


### В docker

В Windows должен быть установлен Docker Desktop.

Выполнить команду сборки образа в терминале
```bash
docker build -t heart-damage-risk-app .
```
Запустить собранный Docker-образ в контейнере
```bash
docker run -d -p 8000:8000 --name heart-damage-risk-app heart-damage-risk-app
```
Открыть в браузере ссылку http://localhost:8000/ 

Оостановить контейнер можно командой:
```bash
docker stop heart-damage-risk-app
```
Посмотреть журнал логов:
```bash
docker logs heart-damage-risk-app
```

## Стек
- Python 3.12
- Pandas
- numpy
- Scikit-learn
- FastAPI
- HTML
