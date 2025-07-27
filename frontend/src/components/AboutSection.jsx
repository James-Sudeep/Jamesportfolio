import React from 'react';
import { Card } from './ui/card';

const AboutSection = ({ data }) => {
  return (
    <section className="about-section">
      <div className="container">
        <div className="section-header">
          <div className="section-badge">🎯 ABOUT ME</div>
          <h2 className="section-title">The Systems Architect Behind the Magic</h2>
          <p className="section-description">
            Transforming complex IT challenges into elegant, scalable solutions that drive business growth and operational excellence.
          </p>
        </div>
        
        <Card className="about-card">
          <div className="about-content">
            <h3 className="about-mission-title">My Mission</h3>
            <p className="about-mission-text">
              {data.about.mission}
            </p>
            
            <h3 className="about-highlights-title">What Sets Me Apart</h3>
            <div className="about-highlights">
              {data.about.highlights.map((highlight, index) => (
                <div key={index} className="highlight-card">
                  <div className="highlight-icon">{highlight.icon}</div>
                  <h4 className="highlight-title">{highlight.title}</h4>
                  <p className="highlight-description">{highlight.description}</p>
                </div>
              ))}
            </div>
          </div>
        </Card>
      </div>
    </section>
  );
};

export default AboutSection;