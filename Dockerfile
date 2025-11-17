FROM python:3.12-alpine
WORKDIR /mini-app-mysql

COPY ./requirements.txt /mini-app-mysql/requirements.txt
RUN pip install -r /mini-app-mysql/requirements.txt

COPY ./app /mini-app-mysql/app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]