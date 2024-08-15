FROM python:3.8.18

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update && apt-get install -y default-mysql-client
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio_api.wsgi:application"]