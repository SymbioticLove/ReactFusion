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
    comp_dir = os.path.join(project_name, "src", "components")
    os.makedirs(data_dir)
    os.makedirs(comp_dir)

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
        
def modify_readme(project_name):
    readme_path = os.path.join(project_name, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "w") as readme_file:
            readme_file.write(
                """# Welcome to React Fusion

React Fusion is a proprietary new framework we are building on top of the React and Git architecture that will allow React developers to create fully-functional MPAs and serverless architectures without ever leaving their React app or having to worry about setting up a back-end system. Currently, there is no styling applied to the app so it looks a little boring, but it's a Ferrari under the hood! This will be updated soon.

## What makes a Fusion app different from a standard React app?
A Fusion app is a specifically structured React/Redux app with additional scripts, dependencies, plugins, and file modifications from a standard React app. Added default dependencies include react-router-dom and react-redux for setting up the default MPA and Provider structure that the larger Fusion framework will work on, and ESLint and Prettier for linting and formatting, amongst others. The create_fusion_app script, which will soon be released to pip, will provide an excellent starting point for ANY React/Redux project, even if you do not plan to use the Fusion framework. From a single command, you are able to create a perfectly structured and formatted Fusion app. Then, simply navigate to the root directory and start the development server with `npm start` as always.

## CreateFusionApp
Within the CreateFusionApp directory, you will find the modularized version of the script to create a Fusion project. To create a Fusion project:

1. Clone this repository
2. Navigate to the CreateFusionApp directory
3. Run the command `fusion` (you can also provide a directory argument for the project here: `fusion c:\` will save the project at the C drive. If no directory argument is provided, the project will be created one directory above the CreateFusionApp directory)
4. Provide a unique project name in the format project-name-formatted
5. Go grab a coffee
6. Navigate to your new project directory
7. Initialize the development server with `npm start`

To note: If you do not have auto-formatting in your IDE tied to Prettier (such as in VSCode), you can format your project by using the command `npm run lint-and-format` in your project's root directory.

## Project structure
The Fusion app structure is as follows:

```
Root/
|-- node_modules/
| |-- ...
|
|-- public/
| |-- ...
|
|-- src/
| |-- App.js (App entry point)
| |-- index.js
| |-- index.css
| |-- setupTests.js
| |-- reportWebVitals.js
|
| |-- redux/
| | |-- reducers.js
| | |-- store.js
|
| |-- data/
| | |-- data.json
|
| |-- components/
| | |-- ...
|
|-- .eslintrc.json
|-- .gitignore
|-- .prettierrc
|-- package.json
|-- index.html
```

## Available scripts in your Fusion app
- `npm start` Start the development server
- `npm run build` Build the production-ready app
- `npm run lint` Run ESLint to check your code for errors and style issues
- `npm run lint:fix` Run ESLint and automatically fix fixable issues
- `npm run format` Run Prettier to format your code
- `npm run lint-and-format` Run ESLint and Prettier together (you'll use this most!)
- `npm run watch-data`: Watch for changes in data files
- `npm run handle-data-change`: Rebuild the app and update data when data files change

The final 2 commands will be used in the future for the larger framework and CMS system that will be built around it but serve no practical purpose currently

## Fusion app code formatting guidelines

### The ESLint configuration (.eslintrc.json) enforces the following rules:
  
1. Line Length: Lines in your code must be 80 characters long or less
2. Indentation: Tab width should be 2
3. String Quotes: Strings should be enclosed in single quotes
4. Trailing Commas: Trailing commas should be included for all items in lists and objects
5. Bracket Spacing: Spaces should be maintained between brackets in object literals
6. Semicolons: Statements should always end with semicolons
7. Arrow Function Parentheses: Single arrow function parameters should not have parentheses
                              
### The Prettier configuration (.prettierrc) enforces the same rules, but focuses on consistency and style instead of code quality. You can modify your .eslintrc.json file to enforce more strict or specific rules such as naming conventions.
     
## A community-driven project

As with a majority of the React ecosystem, React Fusion is also seeking to be driven by an amazing community. We are seeking contributors from a wide variety of disciplines! We have need for AI/ML masters, Python programmers, React experts, testing and debugging experts, websockets experts, and more. If you believe that you can improve Fusion, do not hesitate to pop over to our Boards or Issues sections to tackle a new feature or a known bug or submit a pull request for something else!

### Formatting note for contributors

If you plan to contribute to building the larger framework, you will need to create a virtual environment and install black and flake8 through pip in your virtual environment.

## ReactFusion framework code formatting guidelines

The larger ReactFusion framework (created mainly with Python) uses Flake8 and Black for formatting with the following simple rules:

1. Line Length: Lines should be 88 characters or less
2. Import Sorting: Parentheses should be used for imports with multiple items

- `black --exclude /env .` ran in the root directory of the React Fusion project will format your Python code along these guidelines.

## License

The React Fusion project is an open-source project distributed under the MIT License. You are free to use and customize it for your projects.

### Join the React Fusion community

Follow along with the development of React Fusion by connecting with our CTO on [LinkedIn](https://www.linkedin.com/in/matthew-ford-2a0573272/). Support our development efforts by checking out [our small business](https://symbiotic.love)
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
    while True:
        # Check if a directory argument is provided
        if len(sys.argv) < 2:
            project_path = input("Enter the project directory path: ")
        else:
            project_path = sys.argv[1]

        if os.path.exists(project_path):
            break
        else:
            print("Directory does not exist. Please provide a valid directory path.")

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

    # Modify the README
    modify_readme(project_name)

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
