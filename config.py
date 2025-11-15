import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')  

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or'articlestorage123'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')  
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'articlecms-sqlserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'articlesdb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or'Madavanthi@123'
    SQL_PASSWORD_ENC = quote_plus(SQL_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD_ENC}@{SQL_SERVER}:1433/"
        f"{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')  # keep secret in Azure
    AUTHORITY = 'https://login.microsoftonline.com/eaef6774-977d-450a-9e6c-9e652e39fb95'
    CLIENT_ID = 'a5623f84-9d09-4cc9-8867-b713186a486c'
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    # Session
    SESSION_TYPE = "filesystem"
