import os
import subprocess
import re
import shutil
import json
import sys


# Function to run a shell command
def run_command(command, cwd):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd
    )
    out, err = process.communicate()
    if process.returncode != 0:
        raise Exception(
            f"Error running command: {command}\nError message: {err.decode()}"
        )
    return out.decode()


# Function to validate snake_case_with_dashes
def is_snake_case_with_dashes(name):
    return bool(re.match(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$", name))


# Function to initialize a CRA project
def create_react_app(project_name):
    # Create the React app using CRA
    run_command(
        f"npx create-react-app {project_name} --use-npm --template cra-template",
        cwd=os.getcwd(),
    )

    # Move all files and directories up one level
    inner_dir = os.path.join(project_name, project_name)
    if os.path.exists(inner_dir):
        for item in os.listdir(inner_dir):
            s = os.path.join(inner_dir, item)
            d = os.path.join(project_name, item)
            shutil.move(s, d)

        # Remove the inner folder
        shutil.rmtree(inner_dir)


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


# Function to create a 'data' directory and 'data.json' file within 'src'
def create_data_dir(project_name):
    data_dir = os.path.join(project_name, "src", "data")
    os.makedirs(data_dir)

    # Define the JSON data structure to initialize
    data = {
        "homepage": {
            "welcome": "Welcome to a New Way to Build MPAs and Serverless Architectures with React Fusion"
        }
    }

    # Write the JSON data to 'data.json'
    with open(os.path.join(data_dir, "data.json"), "w") as data_file:
        json.dump(data, data_file, indent=2)


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


# Function to modify the manifest.json file
def modify_manifest_json(project_name):
    manifest_path = os.path.join(project_name, "public", "manifest.json")

    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as manifest_file:
            manifest_data = json.load(manifest_file)

        # Modify the manifest data
        manifest_data["short_name"] = "Fusion App"
        manifest_data["name"] = "Fusion App Skeleton"
        manifest_data["icons"] = []

        # Write the modified data back to the file
        with open(manifest_path, "w") as manifest_file:
            json.dump(manifest_data, manifest_file, indent=2)


# Function to modify the index.css file
def modify_index_css(project_name):
    index_css_path = os.path.join(project_name, "src", "index.css")

    if os.path.exists(index_css_path):
        with open(index_css_path, "w") as index_css_file:
            index_css_file.write(
                """body {
  margin: 0;
  background: #333;
}

html {
  font-size: 100%;
}

:root {
  
}
"""
            )


# Function to modify the index.html file
def modify_index_html(project_name):
    index_html_path = os.path.join(project_name, "public", "index.html")

    if os.path.exists(index_html_path):
        with open(index_html_path, "r") as index_html_file:
            index_html_content = index_html_file.read()

        # Modify the content as needed
        index_html_content = index_html_content.replace(
            "<title>React App</title>", "<title>Fusion App</title>"
        )
        index_html_content = re.sub(
            r'<meta\s+name="description"\s+content="Web site created using create-react-app"\s+/>',
            '<meta name="description" content="Web application created with React Fusion" />',
            index_html_content,
        )
        index_html_content = index_html_content.replace('lang="en"', 'lang="en-US"')
        index_html_content = index_html_content.replace(
            "<!--\n      This HTML file is a template.\n      If you open it directly in the browser, you will see an empty page.\n\n      You can add webfonts, meta tags, or analytics to this file.\n      The build step will place the bundled scripts into the <body> tag.\n\n      To begin the development, run `npm start` or `yarn start`.\n      To create a production bundle, use `npm run build` or `yarn build`.\n    -->",
            "<!--\n      This is where your dynamic content will be rendered. Fusion is built on top\n      of the React library. If you are unfamiliar with React, you should consult\n      their developer documentation as well as the Fusion documentation.\n    -->",
        )

        # Write the modified content back to the file
        with open(index_html_path, "w") as index_html_file:
            index_html_file.write(index_html_content)

    # Install dependencies using npm in the project directory
    run_command(
        f"npm install --save @emailjs/browser @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome @testing-library/jest-dom @testing-library/react @testing-library/user-event date-fns emailjs-com eslint gsap prettier prop-types react react-dom react-scripts react-transition-group redux react-redux web-vitals react-router-dom @reduxjs/toolkit",
        cwd=os.path.join(os.getcwd(), project_name),
    )

    # Install devDependencies using npm in the project directory
    run_command(
        f"npm install --save-dev @babel/plugin-proposal-private-property-in-object eslint-config-prettier eslint-plugin-prettier",
        cwd=os.path.join(os.getcwd(), project_name),
    )

    # Add the specified scripts to the "scripts" section
    package_json_path = os.path.join(project_name, "package.json")
    if os.path.exists(package_json_path):
        with open(package_json_path, "r") as package_json_file:
            package_json = json.load(package_json_file)
            package_json["scripts"]["lint"] = "eslint src"
            package_json["scripts"]["lint:fix"] = "eslint src --fix"
            package_json["scripts"][
                "format"
            ] = 'npx prettier --write "src/**/*.{js,css}"'
            package_json["scripts"][
                "lint-and-format"
            ] = "npm run format && npm run lint:fix"
            package_json["scripts"]["watch-data"] = "npm run handle-data-change"
            package_json["scripts"][
                "handle-data-change"
            ] = "npm run build && rm -rf './src/static/' && mv './src/build/*' './src/'"

        # Update the package.json file
        with open(package_json_path, "w") as package_json_file:
            json.dump(package_json, package_json_file, indent=2)


# Function to move all files and directories up one level
def move_up_and_remove_redundant_dir(project_name):
    for item in os.listdir(project_name):
        s = os.path.join(project_name, item)
        d = os.path.join(os.path.dirname(project_name), item)
        shutil.move(s, d)
    # Remove the redundant directory
    shutil.rmtree(project_name)


# Main function to create the project
def create_project():
    # Check if the user provided a project path as a command-line argument
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        # If no path is provided, create the project in the same directory as the script
        project_path = os.path.abspath(os.path.dirname(__file__))

    # Ensure the project path ends with a trailing slash
    project_path = os.path.join(project_path, "")

    while True:
        # Prompt the user for a snake_case_with_dashes project name
        project_name = input("Enter a project name (project-name): ")
        if not is_snake_case_with_dashes(project_name):
            print("Invalid project name. Please use the format 'project-name'.")
            continue

        # Replace underscores with dashes in the project name
        project_name = project_name.replace("_", "-")

        # Combine the project path and project name to get the full project directory
        project_dir = os.path.join(project_path, project_name)

        # Check if the directory already exists
        if os.path.exists(project_dir):
            print("Project directory already exists. Please choose a different name.")
        else:
            break

    # Create the directory with the project name
    os.makedirs(project_dir)

    # Change directory to the project's root
    os.chdir(project_dir)

    # Create the React app using CRA
    create_react_app(project_name)

    # Set up Redux files
    setup_redux(project_name)

    # Create 'data' directory and 'data.json' file within 'src'
    create_data_dir(project_name)

    # Modify manifest.json
    modify_manifest_json(project_name)

    # Modify the index.html
    modify_index_html(project_name)

    # Modify index.css
    modify_index_css(project_name)

    # Refactor the React app into a Fusion app
    modify_react_project(project_name)

    # Move all files and directories up one level and remove the redundant directory
    move_up_and_remove_redundant_dir(project_name)

    # Ensure proper Fusion formatting
    run_command("npm run lint-and-format", cwd=project_dir)


if __name__ == "__main__":
    create_project()
    print(
        "Project initialization complete. Navigate to your project's source directory and run 'npm start' to initialize the dev server"
    )
