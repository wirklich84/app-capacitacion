import asyncio
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config.config import Settings
from models.user import User

settings = Settings()

async def iniciar_db():
    cliente = AsyncIOMotorClient(settings.db_url_mongo)    
    await init_beanie(database=cliente.sf_encuestas_it, document_models=[User])