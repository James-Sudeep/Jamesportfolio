from models import (
    PortfolioData, PersonalInfo, ContactInfo, Statistic, AboutInfo, Highlight,
    WorkExperience, Project, ProjectImpact, Education, Certification, Credentials
)
from database import get_collection, Collections
import asyncio

# This is the same mock data from frontend, converted to backend models
def get_portfolio_seed_data() -> PortfolioData:
    return PortfolioData(
        personal=PersonalInfo(
            name="Sudeep Siringi",
            title="Senior SCCM Systems Engineer",
            subtitle="Enterprise IT Infrastructure Specialist with 10+ Years of Excellence",
            contact=ContactInfo(
                phone="+91 9008384131",
                email="james.btech16@gmail.com",
                location="Bengaluru, Karnataka, India"
            ),
            stats=[
                Statistic(number="10+", label="Years of Excellence"),
                Statistic(number="99%", label="Customer Satisfaction"),
                Statistic(number="25K+", label="Users Supported"),
                Statistic(number="$1.5M", label="Cost Savings Delivered")
            ]
        ),
        
        about=AboutInfo(
            mission="I architect and optimize enterprise-grade SCCM infrastructures that transform IT operations. With over 10 years of experience managing complex systems for global organizations like Merck Group and IBM, I've mastered the art of turning technical challenges into business solutions.",
            highlights=[
                Highlight(
                    icon="🎯",
                    title="Strategic Systems Design",
                    description="I don't just manage systems—I architect scalable IT infrastructures that drive business growth and operational excellence."
                ),
                Highlight(
                    icon="⚡",
                    title="Performance Excellence",
                    description="Consistently achieving 99% customer satisfaction and quality scores through proactive system optimization and user-centric support."
                ),
                Highlight(
                    icon="🏆",
                    title="Enterprise Leadership",
                    description="Leading digital transformation initiatives and mentoring teams while maintaining industry-leading service standards."
                )
            ]
        ),
        
        skills={
            "🎯 SCCM & Endpoint Management": [
                "SCCM Architecture & Administration",
                "Software Distribution & Deployment", 
                "OS Imaging & Deployment",
                "Patch Management",
                "Compliance Monitoring",
                "PowerShell Automation",
                "Asset Management",
                "Remote Administration"
            ],
            "🏗️ Infrastructure & Cloud": [
                "Active Directory",
                "Windows Server Administration",
                "Virtual Desktop Infrastructure (VDI)",
                "Citrix XenApp/XenDesktop",
                "Network Troubleshooting",
                "DNS/DHCP Management",
                "System Monitoring",
                "Backup & Recovery"
            ],
            "🔒 Security & Compliance": [
                "SSO Implementation & Troubleshooting",
                "RSA Authentication",
                "DOD Security Standards",
                "User Access Management",
                "Security Policy Enforcement",
                "Vulnerability Assessment",
                "Identity Management",
                "Compliance Auditing"
            ],
            "🛠️ Enterprise Platforms": [
                "ServiceNow ITSM",
                "Microsoft 365 Administration",
                "JIRA & Confluence",
                "SAP Systems Support",
                "Oracle Database Management",
                "ITIL Framework",
                "Vendor Management",
                "SLA Management"
            ]
        },
        
        experience=[
            WorkExperience(
                id=1,
                period="Dec 2019 - Present",
                title="Senior System Engineer",
                company="Merck Group",
                type="Global Pharmaceutical Leader",
                achievements=[
                    "Maintained industry-leading 99% customer satisfaction across 25,000+ user interactions",
                    "Spearheaded enterprise SCCM infrastructure supporting life sciences operations",
                    "Implemented zero-downtime system migrations and software deployments",
                    "Led digital transformation initiatives reducing operational costs by 35%",
                    "Established automated troubleshooting processes improving resolution time by 60%",
                    "Mentored junior engineers and conducted technical training sessions"
                ],
                technologies=["SCCM", "ServiceNow", "Active Directory", "Citrix", "PowerShell"]
            ),
            WorkExperience(
                id=2,
                period="Jun 2016 - Dec 2019",
                title="Technical Support Officer",
                company="Marlabs Software",
                type="Enterprise Solutions Provider",
                achievements=[
                    "Provided L1/L2/L3 support for enterprise clients including pharmaceutical giants",
                    "Managed complex VDI environments supporting 1000+ concurrent users",
                    "Implemented RSA authentication and DOD security compliance frameworks",
                    "Reduced ticket resolution time by 45% through process optimization",
                    "Established vendor relationships and SLA management protocols",
                    "Achieved 98% first-call resolution rate for critical incidents"
                ],
                technologies=["VDI", "Citrix", "RSA", "Active Directory", "Network Administration"]
            ),
            WorkExperience(
                id=3,
                period="Dec 2014 - Jun 2016", 
                title="Desktop Support Engineer",
                company="IBM",
                type="Global Technology Services",
                achievements=[
                    "Managed enterprise desktop environments for Fortune 500 legal clients",
                    "Implemented BYOD solutions using Citrix Worx for mobile workforce",
                    "Maintained comprehensive asset management and inventory systems",
                    "Executed Windows 7/8/10 deployments and system upgrades",
                    "Established IT service delivery standards and documentation",
                    "Achieved 97% user satisfaction in service delivery metrics"
                ],
                technologies=["Windows Deployment", "Citrix Worx", "Asset Management", "BYOD"]
            )
        ],
        
        projects=[
            Project(
                id=1,
                number="01",
                title="Global SCCM Infrastructure Transformation",
                description="Architected and deployed comprehensive SCCM infrastructure for pharmaceutical giant supporting 15,000+ endpoints across 30+ global locations with zero-downtime migration.",
                impact=ProjectImpact(
                    title="🎯 Business Impact",
                    metrics=[
                        "Reduced software deployment time by 70%",
                        "Achieved 99.8% system uptime during migration",
                        "Generated $1.5M annual operational savings",
                        "Eliminated 150+ manual hours monthly"
                    ]
                ),
                technologies=["SCCM", "PowerShell", "SQL Server", "Active Directory", "Group Policy"]
            ),
            Project(
                id=2,
                number="02",
                title="Enterprise VDI Optimization Project",
                description="Designed and implemented scalable VDI solution using Citrix technologies supporting 1000+ concurrent users with advanced security and performance optimization.",
                impact=ProjectImpact(
                    title="⚡ Technical Achievement", 
                    metrics=[
                        "Improved user login time by 60%",
                        "Reduced infrastructure costs by 40%",
                        "Achieved 99.5% availability SLA",
                        "Enhanced security compliance by 95%"
                    ]
                ),
                technologies=["Citrix XenDesktop", "VDI", "Storage Optimization", "Load Balancing"]
            ),
            Project(
                id=3,
                number="03",
                title="ServiceNow ITSM Implementation",
                description="Led enterprise-wide ServiceNow implementation transforming IT service delivery and establishing automated workflows for 25,000+ users across multiple business units.",
                impact=ProjectImpact(
                    title="🌟 Operational Excellence",
                    metrics=[
                        "Improved ticket resolution by 65%",
                        "Automated 80% of routine tasks",
                        "Achieved 99% customer satisfaction",
                        "Reduced service delivery costs by 30%"
                    ]
                ),
                technologies=["ServiceNow", "ITIL", "Workflow Automation", "Integration APIs"]
            ),
            Project(
                id=4,
                number="04",
                title="Security & Compliance Framework",
                description="Implemented comprehensive security framework incorporating RSA authentication, DOD standards, and advanced threat protection for life sciences organization.",
                impact=ProjectImpact(
                    title="🔒 Security Excellence",
                    metrics=[
                        "Achieved 100% compliance with DOD standards",
                        "Reduced security incidents by 85%",
                        "Implemented zero-trust architecture",
                        "Enhanced audit readiness by 90%"
                    ]
                ),
                technologies=["RSA SecurID", "DOD Compliance", "SSO", "Security Hardening"]
            ),
            Project(
                id=5,
                number="05",
                title="Automated Patch Management System",
                description="Developed intelligent patch management system using SCCM and PowerShell automation, ensuring enterprise-wide security compliance with minimal business disruption.",
                impact=ProjectImpact(
                    title="🤖 Automation Success",
                    metrics=[
                        "Reduced patch deployment time by 80%",
                        "Achieved 99.5% patch compliance rate",
                        "Eliminated weekend maintenance windows",
                        "Saved 200+ hours monthly through automation"
                    ]
                ),
                technologies=["SCCM", "PowerShell", "WSUS", "Automation Scripts"]
            ),
            Project(
                id=6,
                number="06",
                title="Digital Workplace Transformation",
                description="Spearheaded complete digital workplace transformation including Microsoft 365 implementation, mobile device management, and modern authentication systems.",
                impact=ProjectImpact(
                    title="🚀 Digital Innovation",
                    metrics=[
                        "Enabled 100% remote work capability",
                        "Improved collaboration efficiency by 75%",
                        "Reduced IT support tickets by 50%",
                        "Enhanced employee productivity by 40%"
                    ]
                ),
                technologies=["Microsoft 365", "Intune", "Azure AD", "Modern Authentication"]
            )
        ],
        
        credentials=Credentials(
            education=[
                Education(
                    degree="Bachelor of Technology",
                    field="Information Technology", 
                    institution="JNTU University",
                    year="2014"
                ),
                Education(
                    degree="Diploma",
                    field="Electrical and Electronics Engineering",
                    institution="Dr. B. V. Raju Foundations",
                    year="2012"
                )
            ],
            certifications=[
                Certification(
                    name="HCL Certified Network Specialist",
                    issuer="HCL Career Development Center",
                    year="2016"
                ),
                Certification(
                    name="Master Diploma in Computer Hardware", 
                    issuer="Hardware Training Institute",
                    year="2015"
                )
            ]
        )
    )

async def seed_portfolio_data():
    """Seed the database with portfolio data"""
    try:
        collection = await get_collection(Collections.PORTFOLIO_DATA)
        
        # Check if data already exists
        existing = await collection.find_one({})
        if existing:
            print("📋 Portfolio data already exists, skipping seed")
            return
        
        # Insert seed data
        portfolio_data = get_portfolio_seed_data()
        result = await collection.insert_one(portfolio_data.dict())
        
        if result.acknowledged:
            print("✅ Portfolio data seeded successfully")
        else:
            print("❌ Failed to seed portfolio data")
            
    except Exception as e:
        print(f"❌ Error seeding portfolio data: {e}")
        raise

if __name__ == "__main__":
    # Run seeding script
    asyncio.run(seed_portfolio_data())