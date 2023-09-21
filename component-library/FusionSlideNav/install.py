import os
import shutil
import json

# Define the source directory (your component's directory)
component_dir = os.path.dirname(__file__)

# Define the target directory in the user's project
target_dir = os.path.join(
    os.getcwd(), "components"
)  # Adjust the target directory as needed

# Copy files to the target directory
shutil.copytree(component_dir, target_dir)

# Append dataObject.json to data.json
data_object_path = os.path.join(target_dir, "data", "dataObject.json")
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
