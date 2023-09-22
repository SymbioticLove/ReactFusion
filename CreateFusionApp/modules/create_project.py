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
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

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
    print("Project initialization complete.")
