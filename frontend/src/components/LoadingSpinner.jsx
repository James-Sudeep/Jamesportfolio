import React from 'react';

const LoadingSpinner = ({ size = 'medium', message = 'Loading...' }) => {
  const sizeClasses = {
    small: 'w-6 h-6',
    medium: 'w-12 h-12',
    large: 'w-16 h-16'
  };

  return (
    <div className="loading-container">
      <div className={`loading-spinner ${sizeClasses[size]}`}>
        <div className="spinner-ring"></div>
      </div>
      {message && <p className="loading-message">{message}</p>}
    </div>
  );
};

export const SkeletonCard = () => (
  <div className="skeleton-card">
    <div className="skeleton-header"></div>
    <div className="skeleton-content">
      <div className="skeleton-line"></div>
      <div className="skeleton-line short"></div>
      <div className="skeleton-line"></div>
    </div>
  </div>
);

export const SkeletonStats = () => (
  <div className="skeleton-stats">
    {[1, 2, 3, 4].map(i => (
      <div key={i} className="skeleton-stat-card">
        <div className="skeleton-number"></div>
        <div className="skeleton-label"></div>
      </div>
    ))}
  </div>
);

export default LoadingSpinner;