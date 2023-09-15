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
