from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
import os
from typing import Optional

class Database:
    client: Optional[AsyncIOMotorClient] = None
    
    @classmethod
    async def get_database(cls) -> AsyncIOMotorClient:
        """Get database instance"""
        if cls.client is None:
            mongo_url = os.environ.get('MONGO_URL')
            if not mongo_url:
                raise ValueError("MONGO_URL environment variable is required")
            
            cls.client = AsyncIOMotorClient(mongo_url)
        
        db_name = os.environ.get('DB_NAME', 'portfolio_db')
        return cls.client[db_name]
    
    @classmethod
    async def close_database_connection(cls):
        """Close database connection"""
        if cls.client:
            cls.client.close()
            cls.client = None

class Collections:
    """Database collection names"""
    PORTFOLIO_DATA = "portfolio_data"
    CONTACT_MESSAGES = "contact_messages"
    SITE_VISITS = "site_visits"

async def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    """Get a specific collection"""
    db = await Database.get_database()
    return db[collection_name]

async def init_database():
    """Initialize database with indexes and default data"""
    try:
        # Create indexes for better performance
        portfolio_collection = await get_collection(Collections.PORTFOLIO_DATA)
        await portfolio_collection.create_index("created_at")
        
        contact_collection = await get_collection(Collections.CONTACT_MESSAGES)
        await contact_collection.create_index("timestamp")
        await contact_collection.create_index("status")
        await contact_collection.create_index("reference_id", unique=True)
        
        visits_collection = await get_collection(Collections.SITE_VISITS)
        await visits_collection.create_index("timestamp")
        await visits_collection.create_index("page")
        
        print("✅ Database initialized successfully")
        
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        raise