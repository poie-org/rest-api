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
            print("예측")
            print(str(prediction))
            predict_class = np.argmax(prediction[0])
            print(str(prediction[0]))

            result = {
                "id": int(predict_class),
                "sound_name": sound_names[predict_class],
                "link": "haha"
            }

            # 결과 저장

            return result

        except Exception as e:
            print("오류 발생 : " + str(e))
