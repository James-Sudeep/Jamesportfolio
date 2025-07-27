import React from 'react';
import { Card } from './ui/card';

const SkillsSection = ({ data }) => {
  return (
    <section className="skills-section">
      <div className="container">
        <div className="section-header">
          <div className="section-badge">⚡ EXPERTISE</div>
          <h2 className="section-title">Technical Mastery & Core Competencies</h2>
          <p className="section-description">
            A comprehensive arsenal of cutting-edge technologies and methodologies that power enterprise transformation.
          </p>
        </div>
        
        <div className="skills-grid">
          {Object.entries(data.skills).map(([category, skills], index) => (
            <Card key={index} className="skill-category">
              <h3 className="skill-category-title">{category}</h3>
              <div className="skill-items">
                {skills.map((skill, skillIndex) => (
                  <span 
                    key={skillIndex} 
                    className="skill-item"
                    style={{ animationDelay: `${skillIndex * 0.1}s` }}
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default SkillsSection;