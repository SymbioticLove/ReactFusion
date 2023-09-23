import React, { useState } from 'react';
import { useSelector } from 'react-redux';

// import FusionSlideNav nested component
import FusionSlideNav from '../FusionSlideNav/FusionSlideNav';

// Pick style template
import styles from './types/animated.module.css';
// Change this to the appropriate type ^ All sleek headers have an image, title (h1), subtitle (h2), and nav menu image
// All headers are small in size
// All headers have transparent backgrounds
// All headers are fully compatible across all modern devices

// Types are different template style sets which can be further modified to your preferences
// Current templates:
// Basic - A basic sleek header with minimal styling - mostly structural
// Animated - A version of the basic template with added keyframe effects

// If you have any issues using this component, refer to the React Fusion documentation in the components section

// If you are using this component outside of a Fusion project, you will simply need to change the useSelector hook
// to reference the appropriate Redux data (line 23) and change the references in the JSX // DOC //

const FusionSleekHeader = () => {
  // Scope Redux data
  const shdata = useSelector(state => state.about.fusionSleekHeader);

  const [isMenuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!isMenuOpen);
  };

  return (
    <div className={styles.headerContainer}>
      <div>
        <img src={shdata.image} alt="logo" />
        <div>
          <h1>{shdata.title}</h1>
          <h2>{shdata.subtitle}</h2>
        </div>
      </div>
      <button onClick={toggleMenu}>
        {/* Replace with "menu_black.svg" in data object for a dark menu button */}
        <img src={shdata.menuImage} alt="menu" className={styles.menuImage} />
        <FusionSlideNav isOpen={isMenuOpen} onClose={toggleMenu} />
      </button>
    </div>
  );
};

export default FusionSleekHeader;
