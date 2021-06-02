from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.poie_repository import PoieDao
from application.poie_service import PoieService
from api.poie_controller import create_api
from application.audio_convertor import AudioConvertor
from config.config import ModelConfig as mc
from config.config import DbConfig as dc
from keras.models import load_model


def create_app():
    app = Flask(__name__)

    database = create_engine(dc.DB_URL, max_overflow=0, echo=True)
    Session = sessionmaker(bind=database)
    session = Session()

    model_path = mc.MODEL_PATH
    model = load_model(model_path)
    model.summary()

    poie_dao = PoieDao(database, session)

    convertor = AudioConvertor()
    poie_service = PoieService(poie_dao, convertor, model)
    create_api(app, poie_service)

    return app
