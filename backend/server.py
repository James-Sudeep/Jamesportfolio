from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from typing import Dict, Any

# Import our models and services
from models import (
    ContactMessageCreate, ContactResponse, APIResponse, 
    SiteVisitCreate
)
from portfolio_service import PortfolioService, ContactService, AnalyticsService
from database import init_database, Database
from seed_data import seed_portfolio_data

# Setup
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create the main app
app = FastAPI(title="Sudeep Siringi Portfolio API", version="1.0.0")

# Create API router with /api prefix
api_router = APIRouter(prefix="/api")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Portfolio Data Endpoints
@api_router.get("/portfolio/personal")
async def get_personal_info():
    """Get personal information and statistics"""
    try:
        data = await PortfolioService.get_personal_info()
        if data:
            return APIResponse(success=True, data=data)
        else:
            raise HTTPException(status_code=404, detail="Personal information not found")
    except Exception as e:
        logger.error(f"Error fetching personal info: {e}")
        return APIResponse(success=False, error=str(e))

@api_router.get("/portfolio/skills")
async def get_skills():
    """Get technical skills organized by categories"""
    try:
        data = await PortfolioService.get_skills()
        if data:
            return APIResponse(success=True, data=data)
        else:
            raise HTTPException(status_code=404, detail="Skills data not found")
    except Exception as e:
        logger.error(f"Error fetching skills: {e}")
        return APIResponse(success=False, error=str(e))

@api_router.get("/portfolio/experience")
async def get_experience():
    """Get work experience timeline"""
    try:
        data = await PortfolioService.get_experience()
        if data:
            return APIResponse(success=True, data=data)
        else:
            raise HTTPException(status_code=404, detail="Experience data not found")
    except Exception as e:
        logger.error(f"Error fetching experience: {e}")
        return APIResponse(success=False, error=str(e))

@api_router.get("/portfolio/projects")
async def get_projects():
    """Get case studies/projects"""
    try:
        data = await PortfolioService.get_projects()
        if data:
            return APIResponse(success=True, data=data)
        else:
            raise HTTPException(status_code=404, detail="Projects data not found")
    except Exception as e:
        logger.error(f"Error fetching projects: {e}")
        return APIResponse(success=False, error=str(e))

@api_router.get("/portfolio/about")
async def get_about():
    """Get about section content"""
    try:
        data = await PortfolioService.get_about()
        if data:
            return APIResponse(success=True, data=data)
        else:
            raise HTTPException(status_code=404, detail="About data not found")
    except Exception as e:
        logger.error(f"Error fetching about info: {e}")
        return APIResponse(success=False, error=str(e))

@api_router.get("/portfolio/credentials")
async def get_credentials():
    """Get education and certifications"""
    try:
        data = await PortfolioService.get_credentials()
        if data:
            return APIResponse(success=True, data=data)
        else:
            raise HTTPException(status_code=404, detail="Credentials data not found")
    except Exception as e:
        logger.error(f"Error fetching credentials: {e}")
        return APIResponse(success=False, error=str(e))

# Contact Endpoints
@api_router.post("/contact/message", response_model=ContactResponse)
async def submit_contact_message(message_data: ContactMessageCreate):
    """Handle contact form submissions"""
    try:
        message = await ContactService.create_message(message_data)
        if message:
            return ContactResponse(
                success=True,
                message="Message sent successfully",
                reference_id=message.reference_id
            )
        else:
            raise HTTPException(status_code=500, detail="Failed to send message")
    except Exception as e:
        logger.error(f"Error creating contact message: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@api_router.get("/contact/messages")
async def get_contact_messages(limit: int = 50, skip: int = 0):
    """Get all contact messages (admin endpoint)"""
    try:
        messages = await ContactService.get_messages(limit=limit, skip=skip)
        return APIResponse(success=True, data=[msg.dict() for msg in messages])
    except Exception as e:
        logger.error(f"Error fetching contact messages: {e}")
        return APIResponse(success=False, error=str(e))

# Analytics Endpoints
@api_router.post("/analytics/visit")
async def track_visit(visit_data: SiteVisitCreate, request: Request):
    """Track portfolio visits"""
    try:
        # Get client IP
        client_ip = request.client.host if request.client else None
        
        success = await AnalyticsService.track_visit(visit_data, ip_address=client_ip)
        if success:
            return APIResponse(success=True, message="Visit tracked successfully")
        else:
            return APIResponse(success=False, error="Failed to track visit")
    except Exception as e:
        logger.error(f"Error tracking visit: {e}")
        return APIResponse(success=False, error=str(e))

@api_router.get("/analytics/stats")
async def get_analytics_stats(days: int = 30):
    """Get visit statistics"""
    try:
        stats = await AnalyticsService.get_visit_stats(days=days)
        return APIResponse(success=True, data=stats)
    except Exception as e:
        logger.error(f"Error fetching analytics: {e}")
        return APIResponse(success=False, error=str(e))

# Health check endpoint
@api_router.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Sudeep Siringi Portfolio API is running", "status": "healthy"}

@api_router.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        # Test database connection
        data = await PortfolioService.get_personal_info()
        db_status = "connected" if data else "no_data"
        
        return {
            "status": "healthy",
            "database": db_status,
            "message": "Portfolio API is operational"
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            "status": "unhealthy",
            "database": "error",
            "error": str(e)
        }

# Include the API router
app.include_router(api_router)

# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize the application"""
    try:
        logger.info("🚀 Starting Portfolio API...")
        
        # Initialize database
        await init_database()
        
        # Seed portfolio data
        await seed_portfolio_data()
        
        logger.info("✅ Portfolio API started successfully")
        
    except Exception as e:
        logger.error(f"❌ Failed to start Portfolio API: {e}")
        raise

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Clean up resources"""
    try:
        await Database.close_database_connection()
        logger.info("👋 Portfolio API shut down successfully")
    except Exception as e:
        logger.error(f"Error during shutdown: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)