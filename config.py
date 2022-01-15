import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLAlCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    