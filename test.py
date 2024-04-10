import subprocess
import os

collection_name = "me.app"

# Execute ansible-creator command to initialize the collection
try:
    subprocess.run(
        ["ansible-creator", "init", collection_name, "--init-path", "/tmp", "--force"],
        check=True,
    )
except subprocess.CalledProcessError as e:
    error_message = f"Failed to initialize Ansible collection '{collection_name}': {e}"
    raise (error_message)

# Compress the initialized collection into a tarball
tarball_name = f"{str(collection_name.split('.')[0])}.tar.gz"
try:
    subprocess.run(
        ["tar", "-czf", tarball_name, "/tmp/" + str(collection_name.split(".")[0])],
        check=True,
    )
except subprocess.CalledProcessError as e:
    error_message = (
        f"Failed to compress Ansible collection '{collection_name}' into tarball: {e}"
    )
    raise (error_message)
