FROM python:3.9.15


WORKDIR /app


ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "fast:app",  "--reload", "--host" ,"0.0.0.0","--port","5000"]



