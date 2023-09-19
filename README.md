# React Fusion Framework Documentation

This is a comprehensive documentation for using the Fusion React framework. Here you will find everything you need to know to help build the React Fusion framework and build with it.

## Update 0.0.3 - npm Install Script + package.json + 1 more component

I have created an installation script and package.json for the components when they are installed through npm. Ideally, this will make it where you can install individual components on an as-needed basis. When a component is added to the project, the desired behavior is for the types and nested-components directories, as well as the component .js file, to be added to your project's component directory (I need to modify the create project script to also create a components directory - first issue if anyone wants to tackle it!) and for the data object to be appended to your data.json file. Then it's just a matter of plug and play! The current header components do not yet contain a nav menu, but that is the next priority. There are now 2 headers, a fixed header and a sleek header. The current install and package scripts are untested, but I know they are close at least. If anyone spots any errors, feel free to submit a pull request.

## What is the Fusion Framework?

The Fusion framework is a comprehensive React framework being designed to simplify the experience of web development. Fusion apps are, at their core, React/Redux apps. They are formatted in a specific way and use existing libraries in combination with proprietary modules and components to, in the near future, enable React developers to create high-fidelity and fully functional web applications that can be hosted in the static environment provided by GitHub Pages securely, without server components, and without sacrificing any of the functionality you would expect from a back-end system. In addition, through GitHub Actions automations and the Git CLI, this system has the potential to act as a simple and dynamic individualized CMS with much higher performance and control than existing PHP CMS. To simplify the CMS functionality planned for the Fusion framework, a simplified no-code UI will also be built around the system leveraging all of these technologies to deliver a seamless and highly-accessible web development experience. Due to the planned structure of the Fusion framework, it will be accessible and usable by all levels of React developers through the set-up tools, which create well formatted React/Redux apps with formatting/linting files and scripts, the component library which will be usable in any React/Redux project, and the no-code UI which will be usable by any and all. Combining the appropriate project structure and the component library creates the Fusion framework architecture and creates the most seamless user experience

## Contributors

If you would like to contribute to the Fusion project, we welcome you! Take your time to read through the documentation carefully and note the structure of Fusion components and the way they fit into the larger architecture, and how they relate to standard React components and projects. You will notice a few common structural tendencies such as:

- Components start with Fusion, and are concise and descriptive. EX: "FusionFixedHeader" or "FusionSleekHeader"
- Components use mapping over the Redux data to generate page content and remain as concise as possible
- Component data is always scoped with the useSelector hook per individual component
- If data must be passed between components, that data is stored in a useEffect or useContext hook and passed as a prop
- Import statements and comments should be similar for each component
- All Python code should use Flake8 and Black for formatting and styling, and all components should use the ESLint and Prettier setup provided by creating a Fusion application. The details of this formatting are found later in this documentation. Because the formatting guidelines and scripts are automatically created when creating a Fusion project, this is the ideal sandbox to create and test Fusion components and integrations
- Classes are kept as minimal as possible (often only the wrapper div will receive a class)
- Because of the above, CSS template styling relies heavily on the C
- Components should be fully [WCAG compliant](https://www.w3.org/WAI/standards-guidelines/wcag/)

### All components for the component are individually installable through npm and must be structured specifically. To wit:

```
--FusionComponent/
  |--data/
  |  |--dataObject.json
  |
  |--nested-components (if applicable)
  |  |--... (Same structure as parent component, can contain multiple nested-component layers)
  |
  |--types/
  |  |--CSS templates
  |
  |--FusionComponent.js
  |--README.md
  |--install.py
  |--package.json
```

The install.py and package.json scripts are the same for all components (unless you went off the script somewhere). Simply copy these into the root directory of your newly created component

#### install.py

```python
import os
import shutil
import json

# Define the source directory (your component's directory)
component_dir = os.path.dirname(__file__)

# Define the target directory in the user's project
target_dir = os.path.join(os.getcwd(), "components")

# Define the component name (based on the .js file's name)
component_name = os.path.splitext(os.path.basename(__file__))[0]

# Create a directory with the component's name around itself
component_target_dir = os.path.join(target_dir, component_name)

# Copy files to the component directory
shutil.copytree(component_dir, component_target_dir)

# Append dataObject.json to data.json
data_object_path = os.path.join(component_target_dir, "data", "dataObject.json")
data_file_path = os.path.join(os.getcwd(), "data.json")

with open(data_object_path, "r") as data_object_file:
    data_object = json.load(data_object_file)

if os.path.exists(data_file_path):
    with open(data_file_path, "r") as data_file:
        data = json.load(data_file)
else:
    data = {}

data.update(data_object)

with open(data_file_path, "w") as data_file:
    json.dump(data, data_file, indent=2)
```

#### package.json

```json
{
  "name": "your-component",
  "version": "1.0.0",
  "scripts": {
    "postinstall": "python install-script.py"
  },
  "files": [
    "component.js",
    "types",
    "nested-components",
    "data/dataObject.json"
  ]
}
```

After you have created the component js file, at least one template CSS, saved the dataObject properly in the data.json (which will likely read as a syntax error; it should not be within an array):

#### dataObject.json

```json
"fusionFixedHeader": {
  "title": "React Fusion",
  "subtitle": "Empowering React Developers",
  "image": "https://placehold.co/150"
}
```

and added the install.py and package.json scripts to the root directory, simply zip the files and place the zipped files in the root component directory as well, and flag it with "REVIEW". You just built a fusion component! Reward yourself somehow because you deserve it. You've contributed mightily to a project that could change the face of web development

### We welcome contributions from those of any level of experience. There is a project for you!

We are looking for a wide range of developers of all skill levels! Whether you are just starting your journey or are a seasoned veteran looking to contribute to the growth of the industry, there's certainly a project for you! If you are an early developer or designer honing your CSS skills, creating CSS type templates will help you master the power of descending selectors and the cascade. Writing documentation can help you get a much deeper understanding of syntaxes and practical examples of powerful concepts like mapping and Redux. For more mid-level developers we are seeking contributions to our proprietary AI model that will be trained extensively on the Fusion system, WCAG reviews, component design, and project board management (Agile masters!). For veterans, we are looking for assistance deriving the specifics of the CMS architecture and UI/UX for the no-code platform we intend to build on top of the Fusion framework, in addition to assistance in deciding the technology stack of that platform. We will also need websockets experts, engineers intimately familiar with GitHub collaboration (this is my first major collaborative project and I have not worked at an enterprise scale; I need the help!), testing and debugging experts, automations experts, devops engineers; the list rolls on. If you're reading this, you certainly have something that can contribute to the Fusion project. Refer to the Board or Issues sections to get an idea of what we are currently working on, and feel free to submit a pull request if you'd like to do something we haven't thought of!

### Using Fusion Components in Other Projects

The Fusion component library can be used in any ReactJS project. Instructions for modifying the component to work in a standard React app are included in the comments in the component, within the component README, and within the component's section in this documentation

### The Fusion Tech Stack

- ReactJS
- Redux
- ESLint
- Prettier
- Python
- CSS
- GitHub (Pages, Actions, Git)

#### Component Libraries

- EmailJS

### What You Need to Build with Fusion
- Node.js (npm)
- Python

## The Fusion App Setup Tool

The Fusion App setup tool is a Python script that creates a Fusion project with:

- A simple Redux setup with a Provider, reducers, store, and data.json
- ESLint and Prettier dependencies installed, .prettierrc and .eslintrc.json files, and related scripts
- A formatted App component wrapped with the Provider, Router, and with hash routing set up for efficient and seamless MPA development
- Modified index.html, index.css, and manifest.json files to fit into the Fusion structure and define a :root for easy and consistent styling

To create a Fusion project clone the repository, navigate to the CreateFusionApp directory, and run the command `fusion`. You will be prompted to provide a unique project name, then the build process will be executed. You may also provide a directory arugment when running the script to declare a filepath for the project. `fusion c:\` or `fusion c:` will save the project at your C:\ drive. If no directory argument is provided, the project will be saved one directory above the script, alongside the CreateFusionApp directory. Mac/Linux users will need to run the create_fusion_app.py script directly. The following files are modified or created through the build process:

### Fusion App.js:
```javascript
import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './redux/store';

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Router>
          <Routes>
            <Route exact path="/" />
            {/* <Route path="/route1" />
              <Route path="/route2" />
              <Route path="/route3" /> */}
          </Routes>
        </Router>
      </Provider>
    </div>
  );
}

export default App;
```

### Redux Files:

#### Data.json:

```json
{
    
}
```

#### reducers.js:

```javascript
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
```

#### store.js:

```javascript
import { configureStore } from '@reduxjs/toolkit';
import rootReducer from './reducers';

const store = configureStore({
  reducer: rootReducer,
});

export default store;
```

### ESLint and Prettier Files:

#### .eslintrc.json:

```json
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
```

#### .prettierrc:
```json
{
  "printWidth": 80,
  "tabWidth": 2,
  "singleQuote": true,
  "trailingComma": "all",
  "bracketSpacing": true,
  "semi": true,
  "arrowParens": "avoid"
}
```

### Index Files:

#### index.html:

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Web application created with React Fusion" />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>Fusion App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This is where your dynamic content will be rendered. Fusion is built on top
      of the React library. If you are unfamiliar with React, you should consult
      their developer documentation as well as the Fusion documentation.
    -->
  </body>
</html>
```

#### index.css:

```css
body {
  margin: 0;
  background: #333;
}

html {
  font-size: 100%;
}

:root {
}
```

### Manifest and Package files

### manifest.json:

```json
{
  "short_name": "Fusion App",
  "name": "Fusion App Skeleton",
  "icons": [],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
```


### package.json:

```json
{
  "name": "test",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@emailjs/browser": "^3.11.0",
    "@fortawesome/free-solid-svg-icons": "^6.4.2",
    "@fortawesome/react-fontawesome": "^0.2.0",
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "date-fns": "^2.30.0",
    "emailjs-com": "^3.2.0",
    "eslint": "^8.49.0",
    "gsap": "^3.12.2",
    "prettier": "^3.0.3",
    "prop-types": "^15.8.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-redux": "^8.1.2",
    "react-router-dom": "^6.16.0",
    "react-scripts": "^5.0.1",
    "react-transition-group": "^4.4.5",
    "redux": "^4.2.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "lint": "eslint src",
    "lint:fix": "eslint src --fix",
    "format": "npx prettier --write \"src/**/*.{js,css}\"",
    "lint-and-format": "npm run format && npm run lint:fix",
    "watch-data": "npm run handle-data-change",
    "handle-data-change": "npm run build && rm -rf './src/static/' && mv './src/build/*' './src/'"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@babel/plugin-proposal-private-property-in-object": "^7.21.11",
    "eslint-config-prettier": "^9.0.0",
    "eslint-plugin-prettier": "^5.0.0"
  }
}
```

## create_fusion_app.py

create_fusion_app.py is the Python script responsible for setting up the Fusion project. After running the script, simply navigate the the project directory and run `npm start` as always

```python
from create_project import create_project

if __name__ == "__main__":
    create_project()
    print(
        "Project initialization complete. Navigate to your project's source directory and run 'npm start' to initialize the dev server"
    )
```
### create_project.py

The create_project.py module handles a the main workflow of the script. This script can also be ran directly to create a project if the main script is not working. After creating the project, the script formats the project with the new formatting guidelines

```python
import sys
import os
from modules.name_validation import is_snake_case_with_dashes
from modules.create_react_app import create_react_app
from modules.setup_redux import setup_redux
from modules.create_data_dir import create_data_dir
from modules.modify_manifest import modify_manifest_json
from modules.modify_index_css import modify_index_css
from modules.modify_index_html import modify_index_html
from modules.modify_react_project import modify_react_project
from modules.modify_readme import modify_readme
from modules.move_files import move_up_and_remove_redundant_dir
from modules.run_command import run_command


# Main function to create the project
def create_project():
    # Check if the user provided a project path as a command-line argument
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        # If no path is provided, create the project one directory above itself
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

    # Ensure the project path ends with a trailing slash
    project_path = os.path.join(project_path, "")

    while True:
        # Prompt the user for a snake-case-with-dashes project name
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
    print("Project initialization complete.")
```

### run_command.py

The run_command.py module is a utility module used in several other modules to interface with the command line

```python
import subprocess


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
```

### name_validation.py

The name_validation.py module is responsible for validating the appropriate format for the user input name. The correct format is "project-name-formatted", but the script is also set up to handle the case where "project_name_formatted" is entered and replace the characters approrpiately within the while loop in the create_project.py script

```python
import re


# Function to validate snake-case-with-dashes
def is_snake_case_with_dashes(name):
    return bool(re.match(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$", name))
```

### create_react_app.py

The create_react_app.py module is resposible for initializing a standard Create React App with npm. It also removes the redundant directory created in the process

```python
from modules.run_command import run_command
import os
import shutil


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
```

### setup_redux.py

The setup_redux.py module sets up the Redux reducers and store, as well as the redux directory

```python
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

```

### create_data_dir.py

The create_data_dir.py module creates the data directory and intializes the data.json file

```python
import os
import json


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
```

### modify_manifest.py

The modify_mainfest.py module modifies the manifest.json file, removing unnecessary entries

```python
import os
import json


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
```

### modify_index_html.py

The modify_index_html.py module is responsible for modifying the index.html files AND the package.json scripts. This will be separated into 2 different modules in the future

```python
import os
import re
import json
from modules.run_command import run_command


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
        f"npm install --save @emailjs/browser @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome @testing-library/jest-dom @testing-library/react @testing-library/user-event date-fns emailjs-com eslint gsap prettier prop-types react react-dom react-scripts react-transition-group redux react-redux web-vitals react-router-dom",
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
```

### modify_index_css.py

The modify_index_css.py module is responsible for modifying the index.css file to remove unnecessary styles and add a :root for easy and consistent styling

```python
import os


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
```

### modify_readme.py

The modify_readme.py module is responsible for modifying the README files of the created project to reflect its new structure and give instructions for its use

```python
import os


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

(```)
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
(```)

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
```

### modify_react_project.py

The modify_react_project.py module is responsible for setting up the App.js, .eslintrc.json, and .prettierrc files

```python
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
            {/* <Route path="/route1" />
              <Route path="/route2" />
              <Route path="/route3" /> */}
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
```

## Components

Here you will find individuial domumentation for each component within the Fusion library, instructions to modify them for use in standard React projects, and a list of their types. Types are different base stylesheets and can be changed at the top of each component by changing the name before the .module:

#### With the 'basic' stylesheet

```javascript
// Pick style template
import styles from './types/basic.module.css';
```

#### With the 'styled' stylesheet

```javascript
// Pick style template
import styles from './types/styled.module.css';
```

## FusionFixedHeader

All FusionFixedHeader types share the following traits:
1. They are all fixed at the top of the screen
2. They all get smaller as the screen is scrolled
3. They all have an image on the left, a title and subtitle in the center, and a nav menu on the right
4. They all use flexbox styling and are rows on screens larger than 767 pixels and columns on screens smaller

When using the FusionFixedHeader (or any fixed header), your document will be placed BEHIND and UNDERNEATH the header. The element directly after the header will need to account for this!

### Types

- `basic` A simple skeleton template with minimal styling
- `styled` A more styled version with:
    - text shadows
    - a rolling gradient background effect
    - an image hover effect
    - a rounded bottom border when the header shrinks
- `raised` A simple header that appears 3-dimensional with:
    - box-shadow
    - an outset border
    - a rounded bottom border when the header shrinks

### Data Format

Data for the FusionFixedHeader is stored in the data object "fusionFixedHeader" within the about reducer and structured as follows:

```json
{
  "fusionFixedHeader": {
    "title": "React Fusion",
    "subtitle": "Empowering React Developers",
    "image": "https://placehold.co/150"
  }
}
```

Unlike most Fusion components, the FusionFixedHeader renders this data directly instead of with mapping

### To use in a standard ReactJS project

To use the FusionFixedHeader in your standard ReactJS project, you will need to modify the useSelector hook to point to the appropriate page data and modify the references to this page data within the JSX. If you are not using Redux, you will need to remove the useSelector hook, its import, and the data references in the JSX entirely and use your preferred data management technology.

### If using Redux:

Change this line:

```javascript
// Scope Redux data
const fhdata = useSelector(state => state.about.fusionFixedHeader);
```

To use the appropriate data location or useContext data, or however you choose to manage your Redux data, and change the references within the JSX

```javascript
  {fhdata.image}
  {fhdata.title}
  {fhdata.subtitle}
```

### If not using Redux:

Remove the lines:

```javascript
import { useSelector } from 'react-redux';
```

And

```javascript
// Scope Redux data
const fhdata = useSelector(state => state.about.fusionFixedHeader);
```

And remove the references in the JSX:

```javascript
  {fhdata.image}
  {fhdata.title}
  {fhdata.subtitle}
```
