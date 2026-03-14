# Базовый образ с Jupyter Notebook
FROM jupyter/scipy-notebook:latest

# Настройки для запуска Jupyter Notebook
USER jovyan
WORKDIR /home/jovyan/work
EXPOSE 8888

COPY . .

# Запуск Jupyter Notebook
CMD ["jupyter", "notebook", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--ip=0.0.0.0", "--no-browser"]