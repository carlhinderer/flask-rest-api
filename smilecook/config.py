class Config:
    # Flask
    DEBUG = True

    # Secrets
    SECRET_KEY = 'super-secret-key'

    # SqlAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://smilecookuser:smilecookpw@localhost/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
