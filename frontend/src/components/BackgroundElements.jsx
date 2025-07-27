import React from 'react';

const BackgroundElements = () => {
  return (
    <>
      {/* Animated Grid Background */}
      <div className="bg-animation">
        <div className="bg-grid" />
        <div className="floating-orbs">
          <div className="orb orb-1" />
          <div className="orb orb-2" />
          <div className="orb orb-3" />
        </div>
      </div>
    </>
  );
};

export default BackgroundElements;