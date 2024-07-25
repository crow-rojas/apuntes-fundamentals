import React from 'react';
import { DiscussionEmbed } from 'disqus-react';

const Disqus = ({ url, identifier, title }) => {
  const disqusConfig = {
    url,
    identifier,
    title,
  };

  return <DiscussionEmbed shortname="apuntes-fundamentals" config={disqusConfig} />;
};

export default Disqus;
