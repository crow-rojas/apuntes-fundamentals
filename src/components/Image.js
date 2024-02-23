import React from 'react';

const Image = ({ src, alt, width, caption }) => {
  const imagePath = require(`@site/static/img/${src}`).default;

  const figureStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    width: width || 'auto',
    margin: '0 auto',
    marginBottom: '1.5rem',
  };

  const captionStyle = {
    marginTop: '0.5rem',
    marginBottom: '1.5rem',
    fontSize: '0.85rem', // Smaller font size for minimalism
    maxWidth: '80%', // Limiting caption width for better readability
    textAlign: 'center', // Center-align the text
    lineHeight: '1.4', // Improved line height for readability
    fontStyle: 'italic', // A touch of style to differentiate the caption
  };

  return (
    <figure style={figureStyle}>
      <img
        src={imagePath}
        alt={alt}
        style={{ maxWidth: '100%', height: 'auto' }}
      />
      {caption && <figcaption style={captionStyle}>{caption}</figcaption>}
    </figure>
  );
};

export default Image;
