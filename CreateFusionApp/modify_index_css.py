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
