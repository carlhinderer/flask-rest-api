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

    # Flask-Upload
    UPLOADED_IMAGES_DEST = 'static/images'

    # Flask-Caching
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 10 * 60

    # Flask-Limiting
    RATELIMIT_HEADERS_ENABLED = True
