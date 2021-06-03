from config.config import ModelConfig as md
import numpy as np


class PoieService:

    def __init__(self, poie_dao, convertor, model):
        self.poie_dao = poie_dao
        self.convertor = convertor
        self.model = model

    def analysis_audio(self, wave_file):
        sound_names = md.CATEGORIES
        # self.poie_dao.save(wave_file)
        target = self.convertor.convert(wave_file)

        try:
            prediction = self.model.predict(target)
            prediction = prediction[0]
            predict_class = np.argmax(prediction)

            np.set_printoptions(precision=6, suppress=True)

            confidence = prediction[predict_class]
            confidence = round(confidence, 2)
            print("정확도 : " + str(confidence))
            confidence = confidence * 100
            if confidence < 95:
                predict_class = 10  # 정확도가 낮으면 미분류

            result = {
                "id": int(predict_class),
                "sound_name": sound_names[predict_class],
                "confidence": int(confidence),
                "link": "http://localhost:8080/docs/"
            }

            # 결과 저장

            return result

        except Exception as e:
            print("오류 발생 : " + str(e))
