import os


# Function to create a Fusion project
def modify_react_project(project_name):
    with open(os.path.join(project_name, "src", "App.js"), "w") as app_file:
        app_file.write(
            """
import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './redux/store';

import { useSelector } from 'react-redux';

const HomePage = () => {
  const homePageData = useSelector(state => state.about.homepage);
  return (
    <div>
      <h1>{homePageData.welcome}</h1>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Router>
          <Routes>
            <Route exact path="/" element={<HomePage />} />
            <Route path="/route1" />
            <Route path="/route2" />
            <Route path="/route3" />
          </Routes>
        </Router>
      </Provider>
    </div>
  );
}

export default App;
"""
        )

    # Delete specific files
    os.remove(os.path.join(project_name, "src", "logo.svg"))
    os.remove(os.path.join(project_name, "public", "favicon.ico"))
    os.remove(os.path.join(project_name, "public", "logo192.png"))
    os.remove(os.path.join(project_name, "public", "logo512.png"))
    os.remove(os.path.join(project_name, "src", "App.test.js"))
    os.remove(os.path.join(project_name, "src", "App.css"))

    # Create .eslintrc.json and .prettierrc files
    eslint_config = """
{
    "env": {
      "browser": true,
      "es2021": true
    },
    "extends": [
      "eslint:recommended",
      "plugin:react/recommended",
      "plugin:prettier/recommended"
    ],
    "parserOptions": {
      "ecmaVersion": "latest",
      "sourceType": "module"
    },
    "plugins": ["react"],
    "settings": {
      "react": {
        "version": "detect"
      }
    },
    "rules": {},
    "root": true
}
"""
    prettier_config = """
{
  "printWidth": 80,
  "tabWidth": 2,
  "singleQuote": true,
  "trailingComma": "all",
  "bracketSpacing": true,
  "semi": true,
  "arrowParens": "avoid"
}
"""
    with open(os.path.join(project_name, ".eslintrc.json"), "w") as eslint_file:
        eslint_file.write(eslint_config)

    with open(os.path.join(project_name, ".prettierrc"), "w") as prettier_file:
        prettier_file.write(prettier_config)
