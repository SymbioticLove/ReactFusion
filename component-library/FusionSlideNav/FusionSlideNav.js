import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';

// Pick style template
import styles from './types/basic.module.css';
// Change this to the appropriate type ^ All nav bars have 4 links to start
// Since Fusion components use mapping, you simply need to input the correct entries into your data.json
// All SlideNav templates slide in from either the right side or top of screen to reveal a navigation bar
// They slide in from the right on screens greater than 767px and from the top on screens smaller

// IMPORTANT: FusionSlideNave needs to be passed 2 props: isOpen and onClose. Your menu button should pass these
// This is not needed if you are using this within the FusionSleekHeader component, as this is already done
// isOpen is a boolean that determines whether the menu is visible or not
// onClose is a function that is called when the user clicks a link to close the menu
// Refer to the documentation for these props and their prop validation error handling

// Types are different template style sets which can be further modified to your preferences
// Current templates:
// Basic - A simple nav menu with minimal styling and a transparent background

// If you have any issues using this component, refer to the React Fusion documentation in the components section

// If you are using this component outside of a Fusion project, you will simply need to change the useSelector hook
// to reference the appropriate Redux data (line 23) and change the references in the JSX // DOC //

const FusionSlideNav = ({ isOpen, onClose }) => {
  const snd = useSelector(state => state.about.fusionSlideNav);

  const navStyle = {
    display: isOpen ? 'block' : 'none',
  };

  return (
    <div className={styles.slideNavContainer} style={navStyle}>
      <h3>Navigation</h3>
      <ul>
        {snd.routes.map((route, index) => (
          <li key={index}>
            <NavLink to={route.url} activeClassName="active" onClick={onClose}>
              {route.name}
            </NavLink>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Add prop validation with custom error message
FusionSlideNav.propTypes = {
  isOpen: (props, propName, componentName) => {
    if (props[propName] === undefined) {
      return new Error(
        `The prop '${propName}' is required when using '${componentName}' outside of 'ReactSleekHeader'. Refer to the Fusion documentation for more information.`,
      );
    }
    if (typeof props[propName] !== 'boolean') {
      return new Error(
        `Invalid prop '${propName}' supplied to '${componentName}'. It should be a boolean. Refer to the Fusion documentation for more information.`,
      );
    }
    return null;
  },
  onClose: (props, propName, componentName) => {
    if (props[propName] === undefined) {
      return new Error(
        `The prop '${propName}' is required when using '${componentName}' outside of 'ReactSleekHeader'. Refer to the Fusion documentation for more information.`,
      );
    }
    if (typeof props[propName] !== 'function') {
      return new Error(
        `Invalid prop '${propName}' supplied to '${componentName}'. It should be a function. Refer to the Fusion documentation for more information.`,
      );
    }
    return null;
  },
};

export default FusionSlideNav;
