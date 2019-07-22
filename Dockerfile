FROM python:3.7-alpine
RUN mkdir -p app/log
COPY ./app ./app
WORKDIR /app
CMD ["python3", "nginx_log_generator.py"]