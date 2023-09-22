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
