class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://smilecookuser:smilecookpw@localhost/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = '8VWu6vzzA9jfj6qz'
    JWT_ERROR_MESSAGE_KEY = 'message'