FROM python:3.10

WORKDIR /test

COPY . .

RUN pip install -r requirements.txt

CMD [ "pytest", "test_task4.py" ]