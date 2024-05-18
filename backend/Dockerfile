FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENV NAME UvicornApp

CMD ["uvicorn", "--reload", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
