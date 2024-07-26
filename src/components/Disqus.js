import React, { useState } from 'react';
import { DiscussionEmbed } from 'disqus-react';

const Disqus = ({ url, identifier, title }) => {
  const [isBlurred, setIsBlurred] = useState(true);

  const disqusConfig = {
    url,
    identifier,
    title,
  };

  const toggleBlur = () => {
    setIsBlurred(!isBlurred);
  };

  return (
    <div className="disqus-container">
      <button className="toggle-blur-button" onClick={toggleBlur}>
        {isBlurred ? 'Ver' : 'Ocultar'}
      </button>
      <div className={isBlurred ? 'blurred' : ''}>
        <DiscussionEmbed shortname="apuntes-fundamentals" config={disqusConfig} />
      </div>
    </div>
  );
};

export default Disqus;