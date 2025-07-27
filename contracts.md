# Portfolio Backend Integration Contracts

## Overview
This document outlines the backend implementation plan for Sudeep Siringi's SCCM Portfolio website, including API contracts, data models, and integration strategies.

## Current Mock Data Structure

### Personal Information
- Name, title, contact details, location
- Professional summary and statistics
- Years of experience, CSAT scores, achievements

### Skills & Expertise  
- 4 main categories: SCCM & Endpoint Management, Infrastructure & Cloud, Security & Compliance, Enterprise Platforms
- Each category contains multiple technical skills

### Work Experience
- 3 positions: Merck Group (current), Marlabs Software, IBM
- Each includes: period, title, company, achievements, technologies

### Projects/Case Studies
- 6 enterprise transformation projects
- Each includes: title, description, business impact metrics, technologies used

### Education & Certifications
- B.Tech from JNTU, HCL certifications
- Professional credentials and training

## Backend API Design

### Base URL: `${REACT_APP_BACKEND_URL}/api`

### 1. Portfolio Data Endpoints

#### GET /api/portfolio/personal
**Purpose**: Get personal information and statistics
**Response**:
```json
{
  "success": true,
  "data": {
    "name": "Sudeep Siringi",
    "title": "Senior SCCM Systems Engineer", 
    "subtitle": "Enterprise IT Infrastructure Specialist with 10+ Years of Excellence",
    "contact": {
      "phone": "+91 9008384131",
      "email": "james.btech16@gmail.com",
      "location": "Bengaluru, Karnataka, India"
    },
    "stats": [
      {"number": "10+", "label": "Years of Excellence"},
      {"number": "99%", "label": "Customer Satisfaction"},
      {"number": "25K+", "label": "Users Supported"},
      {"number": "$1.5M", "label": "Cost Savings Delivered"}
    ]
  }
}
```

#### GET /api/portfolio/skills
**Purpose**: Get technical skills organized by categories
**Response**:
```json
{
  "success": true,
  "data": {
    "🎯 SCCM & Endpoint Management": [
      "SCCM Architecture & Administration",
      "Software Distribution & Deployment",
      "OS Imaging & Deployment"
    ],
    "🏗️ Infrastructure & Cloud": [...],
    "🔒 Security & Compliance": [...],
    "🛠️ Enterprise Platforms": [...]
  }
}
```

#### GET /api/portfolio/experience
**Purpose**: Get work experience timeline
**Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "period": "Dec 2019 - Present",
      "title": "Senior System Engineer",
      "company": "Merck Group",
      "type": "Global Pharmaceutical Leader",
      "achievements": [...],
      "technologies": [...]
    }
  ]
}
```

#### GET /api/portfolio/projects
**Purpose**: Get case studies/projects
**Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "number": "01",
      "title": "Global SCCM Infrastructure Transformation",
      "description": "...",
      "impact": {
        "title": "🎯 Business Impact",
        "metrics": [...]
      },
      "technologies": [...]
    }
  ]
}
```

#### GET /api/portfolio/about
**Purpose**: Get about section content
**Response**:
```json
{
  "success": true,
  "data": {
    "mission": "I architect and optimize enterprise-grade SCCM infrastructures...",
    "highlights": [
      {
        "icon": "🎯",
        "title": "Strategic Systems Design",
        "description": "..."
      }
    ]
  }
}
```

#### GET /api/portfolio/credentials  
**Purpose**: Get education and certifications
**Response**:
```json
{
  "success": true,
  "data": {
    "education": [...],
    "certifications": [...]
  }
}
```

### 2. Contact & Inquiry Endpoints

#### POST /api/contact/message
**Purpose**: Handle contact form submissions
**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john@company.com", 
  "company": "Tech Corp",
  "message": "Interested in SCCM consulting services",
  "inquiry_type": "consulting" // consulting, employment, collaboration
}
```

**Response**:
```json
{
  "success": true,
  "message": "Message sent successfully",
  "reference_id": "MSG_20250126_001"
}
```

#### GET /api/contact/messages (Admin only)
**Purpose**: Get all contact messages
**Response**: Array of contact messages with timestamps

### 3. Analytics Endpoints (Optional)

#### POST /api/analytics/visit
**Purpose**: Track portfolio visits
**Request Body**:
```json
{
  "page": "home",
  "user_agent": "...",
  "referrer": "...",
  "timestamp": "2025-01-26T10:30:00Z"
}
```

## Database Schema

### Collections/Tables

#### 1. portfolio_data
- Single document containing all portfolio information
- Easily updatable without schema changes
- Fields: personal, skills, experience, projects, about, credentials

#### 2. contact_messages
- Fields: name, email, company, message, inquiry_type, timestamp, status, reference_id

#### 3. site_visits (Optional)
- Fields: page, timestamp, user_agent, referrer, ip_address

## Frontend Integration Plan

### 1. Replace Mock Data
- Remove mock.js imports
- Replace with API calls using axios
- Add loading states and error handling

### 2. API Service Layer
Create `/src/services/portfolioService.js`:
```javascript
import axios from 'axios';

const API_BASE = process.env.REACT_APP_BACKEND_URL + '/api';

export const portfolioService = {
  getPersonalInfo: () => axios.get(`${API_BASE}/portfolio/personal`),
  getSkills: () => axios.get(`${API_BASE}/portfolio/skills`),
  getExperience: () => axios.get(`${API_BASE}/portfolio/experience`),
  getProjects: () => axios.get(`${API_BASE}/portfolio/projects`),
  getAbout: () => axios.get(`${API_BASE}/portfolio/about`),
  getCredentials: () => axios.get(`${API_BASE}/portfolio/credentials`),
  submitContact: (data) => axios.post(`${API_BASE}/contact/message`, data)
};
```

### 3. Component Updates
- Add React hooks for data fetching (useState, useEffect)
- Implement loading states with skeleton components
- Add error handling with toast notifications
- Create contact form with validation

### 4. State Management
- Use React Context or simple state management
- Cache API responses to reduce server calls
- Implement refresh mechanisms

## Implementation Priority

### Phase 1: Core Backend
1. Set up FastAPI backend structure
2. Create MongoDB models for portfolio data
3. Implement basic CRUD endpoints
4. Seed database with mock data

### Phase 2: Frontend Integration  
1. Create API service layer
2. Replace mock data with API calls
3. Add loading states and error handling
4. Implement contact form functionality

### Phase 3: Enhancement
1. Add analytics tracking
2. Implement caching strategies
3. Add admin interface (optional)
4. Performance optimization

## Security Considerations
- Input validation for contact forms
- Rate limiting for API endpoints
- CORS configuration
- Environment variable protection
- Data sanitization

## Performance Optimization
- API response caching
- Image optimization
- Lazy loading for sections
- Database indexing
- CDN integration (future)

This contract ensures seamless integration between the existing frontend and the new backend implementation while maintaining the current user experience and design standards.