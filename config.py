import os

class Config:
    SECRET_KEY = '12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:123456789@localhost/build'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:123456789@localhost/build'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}