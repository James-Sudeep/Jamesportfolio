import React, { useState } from 'react';
import { usePortfolioData, useAnalytics } from '../hooks/usePortfolioData';
import Navigation from './Navigation';
import HeroSection from './HeroSection';
import AboutSection from './AboutSection';
import SkillsSection from './SkillsSection';
import ProjectsSection from './ProjectsSection';
import ExperienceSection from './ExperienceSection';
import ContactSection from './ContactSection';
import BackgroundElements from './BackgroundElements';
import ScrollIndicator from './ScrollIndicator';
import LoadingSpinner, { SkeletonCard } from './LoadingSpinner';
import ErrorBoundary from './ErrorBoundary';

const PortfolioHome = () => {
  const [activeSection, setActiveSection] = useState('home');
  const { data, loading, error } = usePortfolioData();
  const { trackPageView } = useAnalytics();

  const sections = [
    { id: 'home', label: 'Home', component: HeroSection },
    { id: 'about', label: 'About', component: AboutSection },
    { id: 'skills', label: 'Expertise', component: SkillsSection },
    { id: 'projects', label: 'Case Studies', component: ProjectsSection },
    { id: 'experience', label: 'Journey', component: ExperienceSection },
    { id: 'contact', label: 'Connect', component: ContactSection }
  ];

  const handleSectionChange = (sectionId) => {
    setActiveSection(sectionId);
    window.scrollTo({ top: 0, behavior: 'smooth' });
    trackPageView(sectionId);
  };

  // Loading state
  if (loading) {
    return (
      <div className="portfolio-container">
        <BackgroundElements />
        <div className="loading-portfolio">
          <LoadingSpinner size="large" message="Loading Sudeep's Portfolio..." />
          <div className="loading-skeletons">
            <SkeletonCard />
            <SkeletonCard />
            <SkeletonCard />
          </div>
        </div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div className="portfolio-container">
        <BackgroundElements />
        <div className="error-portfolio">
          <div className="error-content">
            <div className="error-icon">⚠️</div>
            <h2 className="error-title">Unable to Load Portfolio</h2>
            <p className="error-message">
              Sorry, we couldn't load Sudeep's portfolio data. Please check your connection and try again.
            </p>
            <p className="error-details">{error}</p>
            <button 
              className="btn-primary"
              onClick={() => window.location.reload()}
            >
              Try Again
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Main portfolio content
  return (
    <ErrorBoundary>
      <div className="portfolio-container">
        <BackgroundElements />
        <ScrollIndicator />
        <Navigation 
          sections={sections}
          activeSection={activeSection}
          onSectionChange={handleSectionChange}
        />
        
        <main className="main-content">
          {sections.map(({ id, component: Component }) => (
            <div 
              key={id}
              className={`section ${activeSection === id ? 'active' : ''}`}
            >
              <Component data={data} onNavigate={handleSectionChange} />
            </div>
          ))}
        </main>
      </div>
    </ErrorBoundary>
  );
};

export default PortfolioHome;