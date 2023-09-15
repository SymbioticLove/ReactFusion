import os


# Function to set up Redux files
def setup_redux(project_name):
    redux_dir = os.path.join(project_name, "src", "redux")
    os.makedirs(redux_dir)
    with open(os.path.join(redux_dir, "reducers.js"), "w") as reducers_file:
        reducers_file.write(
            """
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
"""
        )
    with open(os.path.join(redux_dir, "store.js"), "w") as store_file:
        store_file.write(
            f"""
import {{ configureStore }} from '@reduxjs/toolkit';
import rootReducer from './reducers';

const store = configureStore({{
  reducer: rootReducer,
}});

export default store;
"""
        )
