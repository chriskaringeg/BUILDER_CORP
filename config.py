import os

class Config:
    SECRET_KEY = '12345'
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:123456789@localhost/build'
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://chris:123456789@localhost/builder'
>>>>>>> 0bfcd28e80815d4aaebd1ffd635511b2790808bb
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:123456789@localhost/build'
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://chris:123456789@localhost/builder'
>>>>>>> 0bfcd28e80815d4aaebd1ffd635511b2790808bb
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}