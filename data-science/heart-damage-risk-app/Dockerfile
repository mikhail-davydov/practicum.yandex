FROM python:3.12-alpine

RUN apk update && \
    apk add --no-cache musl-dev gcc g++ linux-headers

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]