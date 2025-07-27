from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid

# Portfolio Data Models
class ContactInfo(BaseModel):
    phone: str
    email: EmailStr
    location: str

class Statistic(BaseModel):
    number: str
    label: str

class PersonalInfo(BaseModel):
    name: str
    title: str
    subtitle: str
    contact: ContactInfo
    stats: List[Statistic]

class Highlight(BaseModel):
    icon: str
    title: str
    description: str

class AboutInfo(BaseModel):
    mission: str
    highlights: List[Highlight]

class WorkExperience(BaseModel):
    id: int
    period: str
    title: str
    company: str
    type: Optional[str] = None
    achievements: List[str]
    technologies: List[str]

class ProjectImpact(BaseModel):
    title: str
    metrics: List[str]

class Project(BaseModel):
    id: int
    number: str
    title: str
    description: str
    impact: ProjectImpact
    technologies: List[str]

class Education(BaseModel):
    degree: str
    field: str
    institution: str
    year: str

class Certification(BaseModel):
    name: str
    issuer: str
    year: str

class Credentials(BaseModel):
    education: List[Education]
    certifications: List[Certification]

class PortfolioData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    personal: PersonalInfo
    about: AboutInfo
    skills: Dict[str, List[str]]
    experience: List[WorkExperience]
    projects: List[Project]
    credentials: Credentials
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# Contact Form Models
class ContactMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    company: Optional[str] = None
    message: str
    inquiry_type: str = "general"  # consulting, employment, collaboration, general
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: str = "new"  # new, read, replied
    reference_id: str = Field(default_factory=lambda: f"MSG_{datetime.now().strftime('%Y%m%d')}_{str(uuid.uuid4())[:6].upper()}")

class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    message: str
    inquiry_type: str = "general"

# Analytics Models (Optional)
class SiteVisit(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    page: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    user_agent: Optional[str] = None
    referrer: Optional[str] = None
    ip_address: Optional[str] = None

class SiteVisitCreate(BaseModel):
    page: str
    user_agent: Optional[str] = None
    referrer: Optional[str] = None

# API Response Models
class APIResponse(BaseModel):
    success: bool
    data: Any = None
    message: Optional[str] = None
    error: Optional[str] = None

class ContactResponse(BaseModel):
    success: bool
    message: str
    reference_id: str