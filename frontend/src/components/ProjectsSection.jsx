import React from 'react';
import { Card } from './ui/card';

const ProjectsSection = ({ data }) => {
  return (
    <section className="projects-section">
      <div className="container">
        <div className="section-header">
          <div className="section-badge">🏆 CASE STUDIES</div>
          <h2 className="section-title">Enterprise Transformations</h2>
          <p className="section-description">
            Real-world challenges transformed into industry-leading solutions with measurable business impact.
          </p>
        </div>
        
        <div className="projects-grid">
          {data.projects.map((project) => (
            <Card key={project.id} className="project-card">
              <div className="project-number">{project.number}.</div>
              <h3 className="project-title">{project.title}</h3>
              <p className="project-description">{project.description}</p>
              
              <div className="project-impact">
                <div className="project-impact-title">{project.impact.title}</div>
                <div className="project-impact-metrics">
                  {project.impact.metrics.map((metric, index) => (
                    <div key={index} className="impact-metric">
                      • {metric}
                    </div>
                  ))}
                </div>
              </div>
              
              <div className="project-technologies">
                {project.technologies.map((tech, index) => (
                  <span key={index} className="tech-tag">
                    {tech}
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

export default ProjectsSection;