FROM python:3.11

WORKDIR /app

COPY requirments.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
