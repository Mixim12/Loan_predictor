FROM python:3.11.5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD ["python", "python_app/main.py"]
