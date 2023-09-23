import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';

// Import FusionSimpleNav
import FusionSimpleNav from '/nested-components/FusionSimpleNav/FusionSimpleNav';

// Pick style template
import styles from './types/styled.module.css';
// Change this to the appropriate type ^ All fixed headers have an image, title (h1), subtitle (h2), and nav menu (nested)
// All of the headers will stick to the top of the screen and shrink when the page is scrolled
// All headers are fully compatible across all modern devices

// Types are different template style sets which can be further modified to your preferences
// Current templates:
// Basic - A basic fixed header with a solid background and the described elements
// Styled - A more stylized version of the basic template
// Raised - A header that appears to be 3-dimensional with outset border and box-shadow effects

// If you have any issues using this component, refer to the React Fusion documentation in the components section

// If you are using this component outside of a Fusion project, you will simply need to change the useSelector hook
// to reference the appropriate Redux data (line 24) and change the references in the JSX

const FusionFixedHeader = () => {
  // State to track whether the screen has been scrolled
  const [isScrolled, setIsScrolled] = useState(false);

  // Scope Redux data
  const fhdata = useSelector(state => state.about.fusionFixedHeader);

  // Handle scroll event
  const handleScroll = () => {
    if (window.scrollY > 50) {
      setIsScrolled(true);
    } else {
      setIsScrolled(false);
    }
  };

  // Add and remove scroll event listener
  useEffect(() => {
    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div
      className={`${styles.headerContainer} ${
        isScrolled ? styles.scrolledHeader : ''
      }`}
    >
      <div>
        <img src={fhdata.image} alt="Logo" />
      </div>
      <div>
        <h1>{fhdata.title}</h1>
        <h2>{fhdata.subtitle}</h2>
      </div>
      <FusionSimpleNav />
    </div>
  );
};

export default FusionFixedHeader;
