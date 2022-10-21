class Config:
    """Base config."""
    BASE_URL= 'http://localhost:5555/'

class ProdConfig(Config):
    """config for production environment."""
    MONGO_URI='mongodb://localhost:27017'
    DB_NAME='telegram_bot'  


class TestingConfig(Config):
    """config for testing environment."""
    MONGO_URI='mongodb://localhost:27017'
    DB_NAME='telegram_bot_test' 
