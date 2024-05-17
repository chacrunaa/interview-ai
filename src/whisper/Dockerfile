FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir torch==1.7.1
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

CMD ["python", "transcribe.py"]
