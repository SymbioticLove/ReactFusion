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
