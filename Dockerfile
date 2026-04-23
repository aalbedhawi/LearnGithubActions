
FROM python:3.13

WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt

CMD ["pytest", "--cov=mycalculator", "--cov-fail-under=80"]
