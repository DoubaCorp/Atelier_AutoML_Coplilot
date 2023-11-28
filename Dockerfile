FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./app_consuming /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "weather_app:app", "--host", "0.0.0.0", "--port", "80"]