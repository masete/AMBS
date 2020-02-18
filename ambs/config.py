import os

class BaseConfig:
    """ Project environment configurations """
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    ENV = 'production'
    # DEBUG = False
    # TESTING = False
    DATABASE_URL = 'postgres://qxunsdbokdvold:ccd98e6f32a2d6b455dd941cf19bb1a5a12cb0b8d5ee8ff998c3c5d8a041322a@ec2-52-203-160-194.compute-1.amazonaws.com:5432/dartm9a0g4f4f0'

env_config = dict(
    # development = DevelopmentConfig,
    # testing = TestingConfig,
    production=ProductionConfig
)