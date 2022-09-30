import os
from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    
    db_url_mongo = os.getenv('MONGO_URL')