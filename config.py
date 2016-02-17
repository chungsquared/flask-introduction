import os

# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\xa3\x92\xa3\x1d\xc1sq\xdd\xe3v\xc4\xd5\x14\x06\xd4\x03\xb7Kf\x1e\xf4B\x90\x1a'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False 