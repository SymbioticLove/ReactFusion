import os
import shutil


# Function to move all files and directories up one level
def move_up_and_remove_redundant_dir(project_name):
    for item in os.listdir(project_name):
        s = os.path.join(project_name, item)
        d = os.path.join(os.path.dirname(project_name), item)
        shutil.move(s, d)
    # Remove the redundant directory
    shutil.rmtree(project_name)
