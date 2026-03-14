# Yandex Practicum

## Описание

Репозиторий для хранения решений задач из курсов Yandex Practicum. Включает проекты по Data Science, машинному обучению, развёртыванию моделей и работе с Docker.

## Структура проектов

| Раздел | Описание |
|--------|----------|
| [Docker](./docker/) | Сборник полезных Dockerfiles для использования в проектах |
| [Data Science](./data-science/) | Курс Data Science — решения задач машинного обучения |

---

## Docker

### Описание

Набор Dockerfile-конфигураций для запуска различных инструментов машинного обучения и обработки данных в контейнерах.

### Подразделы

| Директория | Описание |
|------------|----------|
| [jupyter-spark](./docker/jupyter-spark/) | Jupyter Server с Spark для обработки больших данных |

---

## Data Science

### Описание

Коллекция проектов, охватывающих различные области машинного обучения: от классических алгоритмов до глубокого обучения, от анализа данных до развёртывания моделей в продакшен.

### Структура проектов (15 директорий)

| Директория | Описание |
|------------|----------|
| [big-data-spark](./data-science/big-data-spark/README.md) | Обработка больших данных с Apache Spark, предсказание стоимости жилья в Калифорнии |
| [carsharing-project](./data-science/carsharing-project/README.md) | Анализ данных каршеринга, прогнозирование спроса на автомобили |
| [computer-vision](./data-science/computer-vision/README.md) | Компьютерное зрение, определение возраста по фотографии |
| [gradient-boost](./data-science/gradient-boost/README.md) | Градиентный бустинг (XGBoost, LightGBM), предсказание цены автомобилей |
| [heart-damage-risk-app](./data-science/heart-damage-risk-app/README.md) | FastAPI-приложение для предсказания риска сердечного приступа |
| [heart-damage-risk-jupiter](./data-science/heart-damage-risk-jupiter/README.md) | Jupyter Notebook с исследованием данных и построением модели предсказания рисков сердечного приступа |
| [hr-analytics-project](./data-science/hr-analytics-project/README.md) | HR-аналитика, предсказание оттока сотрудников |
| [marketing-project](./data-science/marketing-project/README.md) | Маркетинговая аналитика, предсказание вероятности покупки в интернет-магазине в течение 90 дней |
| [ml-in-business](./data-science/ml-in-business/README.md) | Машинное обучение в бизнесе, решение задач для компании «Лукойл» |
| [natural-language-processing](./data-science/natural-language-processing/README.md) | Обработка естественного языка, анализ данных интернет-магазина WikiShop |
| [neuron-network](./data-science/neuron-network/README.md) | Нейронные сети, предсказание температуры звёзд |
| [search-photo-by-text-project](./data-science/search-photo-by-text-project/README.md) | Поиск изображений по текстовому описанию (мультимодальные модели) |
| [supervised-learning](./data-science/supervised-learning/README.md) | Обучение с учителем, оценка качества моделей машинного обучения |
| [telecom-project](./data-science/telecom-project/README.md) | Телекоммуникационная аналитика, предсказание оттока клиентов |
| [time-series-forecasting](./data-science/time-series-forecasting/README.md) | Прогнозирование временных рядов, предсказание заказов такси |

### Основные темы проектов Data Science

- **Обучение с учителем (Supervised Learning)**: классификация и регрессия, оценка качества моделей
- **Обработка естественного языка (NLP)**: анализ текстов, классификация, извлечение сущностей
- **Компьютерное зрение (CV)**: распознавание образов, определение возраста
- **Временные ряды**: прогнозирование, ARIMA, градиентный бустинг для временных рядов
- **Нейронные сети**: глубокое обучение, регрессия на основе нейросетей
- **Градиентный бустинг**: XGBoost, LightGBM, CatBoost
- **Большие данные**: Apache Spark, распределённые вычисления
- **Развёртывание моделей**: FastAPI, Docker

### Используемые технологии

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- TensorFlow
- Keras
- PyTorch
- Apache Spark (PySpark)
- FastAPI
- Matplotlib
- Seaborn
- Statsmodels
- NLTK
- SpaCy

### Навигация по проектам

#### Начинающим рекомендуется начать с:
1. [supervised-learning](./data-science/supervised-learning/README.md) — основы машинного обучения
2. [gradient-boost](./data-science/gradient-boost/README.md) — современные алгоритмы бустинга

#### Продвинутые темы:
1. [neuron-network](./data-science/neuron-network/README.md) — глубокое обучение
2. [computer-vision](./data-science/computer-vision/README.md) — компьютерное зрение
3. [natural-language-processing](./data-science/natural-language-processing/README.md) — обработка текста

#### Практические приложения:
1. [heart-damage-risk-app](./data-science/heart-damage-risk-app/README.md) — развёртывание модели в продакшен
2. [marketing-project](./data-science/marketing-project/README.md) — реальная бизнес-задача
3. [telecom-project](./data-science/telecom-project/README.md) — аналитика оттока клиентов
