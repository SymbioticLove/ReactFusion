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
3. Create a virtual enviroment with `python -m venv env`
4. Activate the virtual environment with `env\Scripts\activate`
5. Run the command `fusion` (you can also provide a directory argument for the project here: `fusion c:\` will save the project at the C drive. If no directory argument is provided, the project will be created one directory above the CreateFusionApp directory)
6. Provide a unique project name in the format project-name-formatted
7. Go grab a coffee
8. Navigate to your new project directory
9. Initialize the development server with `npm start`

To note: If you do not have auto-formatting in your IDE tied to Prettier (such as in VSCode), you can format your project by using the command `npm run lint-and-format` in your project's root directory.

## Project structure
The Fusion app structure is as follows:

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

## Available scripts in your Fusion app
`npm start` Start the development server
`npm run build` Build the production-ready app
`npm run lint` Run ESLint to check your code for errors and style issues
`npm run lint:fix` Run ESLint and automatically fix fixable issues
`npm run format` Run Prettier to format your code
`npm run lint-and-format` Run ESLint and Prettier together (you'll use this most!)
`npm run watch-data`: Watch for changes in data files
`npm run handle-data-change`: Rebuild the app and update data when data files change

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

If you plan to contribute to building the larger framework, you will need to install black and flake8 through pip in your virtual environment.

## ReactFusion framework code formatting guidelines

The larger ReactFusion framework (created mainly with Python) uses Flake8 and Black for formatting with the following simple rules:

1. Line Length: Lines should be 88 characters or less
2. Import Sorting: Parentheses should be used for imports with multiple items

`black --exclude /env .` ran in the root directory of the React Fusion project will format your Python code along these guidelines.

## License

The React Fusion project is an open-source project distributed under the MIT License. You are free to use and customize it for your projects.

### Join the React Fusion community

Follow along with the development of React Fusion by connecting with our CTO on [LinkedIn](https://www.linkedin.com/in/matthew-ford-2a0573272/). Support our development efforts by checking out [our small business](https://symbiotic.love)
"""
            )
