FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -U openai-whisper

CMD ["python", "main.py"]
 ADD source dest