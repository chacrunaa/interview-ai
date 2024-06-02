import multiprocessing
import numpy as np
from flask import request
from flask_restx import Resource, Namespace
from .extensions import db
from .whisper_model import whisper_transcribation
from .models import Transcribation
from .api_model import transcribation_model, transcribation_input_model
from .utils import save_file


ns = Namespace('api')


@ns.route('/video')
class VideoAPI(Resource):
    
    @ns.expect(transcribation_input_model)
    def post(self):       
        if 'file' not in request.files:
            return {"message": "Файл не получен"}, 400

        # Получаем агрумменты и файл
        id = request.values['id']
        file = request.files['file']
         
        if not id:
            return {"message": "ID не получен"}, 400
                   
        # Запускаем скрипт на транскрибацию
        p = multiprocessing.Process(target=whisper_transcribation, args=(save_file(file),))
        p.start()
        
        return {"message": "Запуск скрипта успешен, текст после транскрибации будет добавлен"}, 200
