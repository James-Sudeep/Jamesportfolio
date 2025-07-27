from typing import Optional, Dict, Any, List
from models import PortfolioData, ContactMessage, ContactMessageCreate, SiteVisit, SiteVisitCreate
from database import get_collection, Collections
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class PortfolioService:
    
    @staticmethod
    async def get_portfolio_data() -> Optional[PortfolioData]:
        """Get the main portfolio data"""
        try:
            collection = await get_collection(Collections.PORTFOLIO_DATA)
            data = await collection.find_one({}, sort=[("updated_at", -1)])
            
            if data:
                # Remove MongoDB's _id field
                data.pop('_id', None)
                return PortfolioData(**data)
            return None
            
        except Exception as e:
            logger.error(f"Error fetching portfolio data: {e}")
            return None
    
    @staticmethod
    async def update_portfolio_data(portfolio_data: PortfolioData) -> bool:
        """Update portfolio data"""
        try:
            collection = await get_collection(Collections.PORTFOLIO_DATA)
            portfolio_data.updated_at = datetime.utcnow()
            
            result = await collection.replace_one(
                {},  # Replace the single document
                portfolio_data.dict(),
                upsert=True
            )
            
            return result.acknowledged
            
        except Exception as e:
            logger.error(f"Error updating portfolio data: {e}")
            return False
    
    @staticmethod
    async def get_personal_info() -> Optional[Dict[str, Any]]:
        """Get personal information section"""
        portfolio = await PortfolioService.get_portfolio_data()
        if portfolio:
            return {
                "name": portfolio.personal.name,
                "title": portfolio.personal.title,
                "subtitle": portfolio.personal.subtitle,
                "contact": portfolio.personal.contact.dict(),
                "stats": [stat.dict() for stat in portfolio.personal.stats]
            }
        return None
    
    @staticmethod
    async def get_skills() -> Optional[Dict[str, List[str]]]:
        """Get skills section"""
        portfolio = await PortfolioService.get_portfolio_data()
        if portfolio:
            return portfolio.skills
        return None
    
    @staticmethod
    async def get_experience() -> Optional[List[Dict[str, Any]]]:
        """Get work experience"""
        portfolio = await PortfolioService.get_portfolio_data()
        if portfolio:
            return [exp.dict() for exp in portfolio.experience]
        return None
    
    @staticmethod
    async def get_projects() -> Optional[List[Dict[str, Any]]]:
        """Get projects/case studies"""
        portfolio = await PortfolioService.get_portfolio_data()
        if portfolio:
            return [project.dict() for project in portfolio.projects]
        return None
    
    @staticmethod
    async def get_about() -> Optional[Dict[str, Any]]:
        """Get about section"""
        portfolio = await PortfolioService.get_portfolio_data()
        if portfolio:
            return {
                "mission": portfolio.about.mission,
                "highlights": [highlight.dict() for highlight in portfolio.about.highlights]
            }
        return None
    
    @staticmethod
    async def get_credentials() -> Optional[Dict[str, Any]]:
        """Get credentials section"""
        portfolio = await PortfolioService.get_portfolio_data()
        if portfolio:
            return {
                "education": [edu.dict() for edu in portfolio.credentials.education],
                "certifications": [cert.dict() for cert in portfolio.credentials.certifications]
            }
        return None

class ContactService:
    
    @staticmethod
    async def create_message(message_data: ContactMessageCreate) -> Optional[ContactMessage]:
        """Create a new contact message"""
        try:
            collection = await get_collection(Collections.CONTACT_MESSAGES)
            
            # Create message object
            message = ContactMessage(**message_data.dict())
            
            # Insert into database
            result = await collection.insert_one(message.dict())
            
            if result.acknowledged:
                return message
            return None
            
        except Exception as e:
            logger.error(f"Error creating contact message: {e}")
            return None
    
    @staticmethod
    async def get_messages(limit: int = 50, skip: int = 0) -> List[ContactMessage]:
        """Get contact messages (for admin use)"""
        try:
            collection = await get_collection(Collections.CONTACT_MESSAGES)
            
            cursor = collection.find({}).sort("timestamp", -1).skip(skip).limit(limit)
            messages = []
            
            async for doc in cursor:
                doc.pop('_id', None)
                messages.append(ContactMessage(**doc))
            
            return messages
            
        except Exception as e:
            logger.error(f"Error fetching contact messages: {e}")
            return []
    
    @staticmethod
    async def mark_message_read(message_id: str) -> bool:
        """Mark a message as read"""
        try:
            collection = await get_collection(Collections.CONTACT_MESSAGES)
            
            result = await collection.update_one(
                {"id": message_id},
                {"$set": {"status": "read"}}
            )
            
            return result.modified_count > 0
            
        except Exception as e:
            logger.error(f"Error updating message status: {e}")
            return False

class AnalyticsService:
    
    @staticmethod
    async def track_visit(visit_data: SiteVisitCreate, ip_address: str = None) -> bool:
        """Track a site visit"""
        try:
            collection = await get_collection(Collections.SITE_VISITS)
            
            visit = SiteVisit(**visit_data.dict(), ip_address=ip_address)
            result = await collection.insert_one(visit.dict())
            
            return result.acknowledged
            
        except Exception as e:
            logger.error(f"Error tracking visit: {e}")
            return False
    
    @staticmethod
    async def get_visit_stats(days: int = 30) -> Dict[str, Any]:
        """Get visit statistics"""
        try:
            collection = await get_collection(Collections.SITE_VISITS)
            
            # Get visits from last N days
            from datetime import timedelta
            start_date = datetime.utcnow() - timedelta(days=days)
            
            pipeline = [
                {"$match": {"timestamp": {"$gte": start_date}}},
                {"$group": {
                    "_id": "$page",
                    "count": {"$sum": 1}
                }},
                {"$sort": {"count": -1}}
            ]
            
            result = await collection.aggregate(pipeline).to_list(100)
            
            total_visits = sum(item["count"] for item in result)
            
            return {
                "total_visits": total_visits,
                "page_visits": result,
                "period_days": days
            }
            
        except Exception as e:
            logger.error(f"Error getting visit stats: {e}")
            return {"total_visits": 0, "page_visits": [], "period_days": days}