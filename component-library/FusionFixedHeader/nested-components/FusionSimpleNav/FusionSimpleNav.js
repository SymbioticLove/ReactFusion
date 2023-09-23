import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';

// Pick style template
import styles from './types/bar.module.css';
// Change this to the appropriate type ^ All FusionSimpleNav components are simple nav menus
// It can be used standalone or embedded within other components

// Types are different template style sets which can be further modified to your preferences
// Current templates:
// Basic - A minimally styled basic nav menu
// Bar - Designed to be used as a standalone - A horizontal bar

// If you have any issues using this component, refer to the React Fusion documentation in the components section

// If you are using this component outside of a Fusion project, you will simply need to change the useSelector hook
// to reference the appropriate Redux data (line 21) and change the references in the JSX // DOC //

const FusionSimpleNav = () => {
  const sNavData = useSelector(state => state.about.fusionSimpleNav);

  // State to track whether the screen has been scrolled
  const [isScrolled, setIsScrolled] = useState(false);

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
      className={`${styles.simpleNavContainer} ${
        isScrolled ? styles.scrolledNav : ''
      }`}
    >
      <ul>
        {sNavData.routes.map((route, index) => (
          <li key={index}>
            <NavLink to={route.url} activeClassName="active">
              {route.name}
            </NavLink>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FusionSimpleNav;
