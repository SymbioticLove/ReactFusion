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
