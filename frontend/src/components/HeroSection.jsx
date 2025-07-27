import React, { useEffect, useState } from 'react';
import { Button } from './ui/button';

const HeroSection = ({ data, onNavigate }) => {
  const [displayedTitle, setDisplayedTitle] = useState('');
  const [titleIndex, setTitleIndex] = useState(0);

  useEffect(() => {
    const timer = setTimeout(() => {
      if (titleIndex < data.personal.name.length) {
        setDisplayedTitle(data.personal.name.slice(0, titleIndex + 1));
        setTitleIndex(titleIndex + 1);
      }
    }, 120);

    return () => clearTimeout(timer);
  }, [titleIndex, data.personal.name]);

  return (
    <section className="hero-section">
      <div className="container">
        <div className="hero-content">
          <div className="hero-badge">
            <span className="hero-badge-icon">🚀</span>
            <span>Available for Elite Opportunities</span>
          </div>
          
          <h1 className="hero-title">
            {displayedTitle}
            <span className="cursor">|</span>
          </h1>
          
          <p className="hero-subtitle">
            {data.personal.title}<br />
            {data.personal.subtitle}
          </p>
          
          <div className="hero-cta">
            <Button 
              className="btn-primary"
              onClick={() => onNavigate('projects')}
            >
              View Case Studies
              <span className="btn-arrow">→</span>
            </Button>
            <Button 
              variant="outline"
              className="btn-secondary"
              onClick={() => onNavigate('contact')}
            >
              Let's Connect
              <span className="btn-icon">💬</span>
            </Button>
          </div>
        </div>
        
        <div className="hero-stats">
          {data.stats.map((stat, index) => (
            <div key={index} className="stat-card">
              <div className="stat-number">{stat.number}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default HeroSection;