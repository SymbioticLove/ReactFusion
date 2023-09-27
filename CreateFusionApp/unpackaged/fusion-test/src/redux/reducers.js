
import { combineReducers } from 'redux';

// Read data from the JSON files
import aboutData from '../data/data.json';

// About reducer
const aboutReducer = (state = aboutData, action) => {
  switch (action.type) {
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  about: aboutReducer,
});

export default rootReducer;
