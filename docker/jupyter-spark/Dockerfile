# Базовый образ с Jupyter Notebook
FROM jupyter/scipy-notebook:latest

# Устанавливаем Java (OpenJDK)
USER root
RUN apt-get update && \
    apt-get install -y openjdk-21-jre-headless && \
    apt-get clean

# Настройка переменной JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"

# Устанавливаем Apache Spark
USER root
RUN apt-get update && \
    apt-get install -y wget && \
    wget -q https://dlcdn.apache.org/spark/spark-3.5.7/spark-3.5.7-bin-hadoop3.tgz && \
    tar xf spark-3.5.7-bin-hadoop3.tgz && \
    mv spark-3.5.7-bin-hadoop3 /usr/local/spark && \
    rm spark-3.5.7-bin-hadoop3.tgz && \
    ln -s /usr/local/spark/bin/pyspark /usr/local/bin/pyspark && \
    ln -s /usr/local/spark/bin/spark-submit /usr/local/bin/spark-submit

# Устанавливаем зависимости Python
RUN pip install pyspark==3.5.7

# Настройки для запуска Jupyter Notebook
USER jovyan
WORKDIR /home/jovyan/work
EXPOSE 8888

# Запуск Jupyter Notebook
CMD ["jupyter", "notebook", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--ip=0.0.0.0", "--no-browser"]