import React from 'react';
import { Card } from './ui/card';

const ExperienceSection = ({ data }) => {
  return (
    <section className="experience-section">
      <div className="container">
        <div className="section-header">
          <div className="section-badge">🌟 CAREER JOURNEY</div>
          <h2 className="section-title">A Decade of Excellence</h2>
          <p className="section-description">
            From junior support to elite architect—a journey of continuous growth, innovation, and leadership.
          </p>
        </div>
        
        <div className="timeline">
          {data.experience.map((job, index) => (
            <div key={job.id} className="timeline-item">
              <div className="timeline-dot" />
              <Card className="timeline-content">
                <div className="timeline-date">{job.period}</div>
                <h3 className="timeline-title">{job.title}</h3>
                <div className="timeline-company">
                  {job.company}
                  {job.type && <span className="timeline-type"> ({job.type})</span>}
                </div>
                <ul className="timeline-achievements">
                  {job.achievements.map((achievement, achIndex) => (
                    <li key={achIndex}>{achievement}</li>
                  ))}
                </ul>
                <div className="timeline-technologies">
                  {job.technologies.map((tech, techIndex) => (
                    <span key={techIndex} className="timeline-tech-tag">
                      {tech}
                    </span>
                  ))}
                </div>
              </Card>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ExperienceSection;