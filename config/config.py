class ModelConfig:
    MODEL_PATH = '/Users/yoon/Downloads/0531VGG16-56-300-64(9766)N3L.h5'

    CATEGORIES = ['에어컨', '경적', '사람',
                  '개', '드릴', '엔진 시동',
                  '총', '잭해머', '사이렌',
                  '거리 음악', '미분류']


class DbConfig:
    DB_URL = 'mysql+pymysql://root:1111@127.0.0.1:3306/flask?charset=utf8'
