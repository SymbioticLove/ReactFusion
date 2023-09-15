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
