import os
import whisper
import warnings
import logging
import time

logging.basicConfig(filename='/app/log.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

warnings.simplefilter("ignore")

# Загрузка модели Whisper
video_files = [f for f in os.listdir("/app/videos") if os.path.isfile(os.path.join("/app/videos", f))]


model = whisper.load_model("base")  # Можно выбрать другую модель, например 'small', 'medium', 'large', или 'tiny'
result = whisper.transcribe(audio=video_path)

start_time = time.time()
api_requests = 0

for video_file in video_files:
    video_path = f"/app/videos/{video_file}"
    
    result = model.transcribe(audio=video_path)
    api_requests += 1
    
    text_result_path = f"/app/text/{os.path.splitext(video_file)[0]}.txt"
    
    with open(text_result_path, "w") as file:
        file.write(result["text"])
    
    os.system(f"python main.py --video {video_path}")

end_time = time.time()
execution_time = end_time - start_time

logger.info(f"API requests: {api_requests}")
logger.info(f"Execution time: {execution_time} seconds")
