import React from 'react';

const Navigation = ({ sections, activeSection, onSectionChange }) => {
  return (
    <nav className="main-navigation">
      <ul className="nav-links">
        {sections.map(({ id, label }) => (
          <li key={id}>
            <button
              className={`nav-link ${activeSection === id ? 'active' : ''}`}
              onClick={() => onSectionChange(id)}
            >
              {label}
            </button>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Navigation;