from flask import Flask, jsonify, request, send_file
import subprocess
import os

app = Flask(__name__)


@app.route("/fetch_collection_tar", methods=["POST"])
def fetch_collection_tar():
    # Retrieve data from the request
    data = request.get_json()

    # Get the collection name from the request
    collection_name = data.get("collection_name")

    # Scaffold
    scaffold_collection(collection_name)

    # Call create tarball
    tarball_name = f"{str(collection_name.split('.')[0])}.tar.gz"
    create_tarball(collection_name, tarball_name)

    # Call remove
    remove_scaffolded_collection(collection_name)

    # Check if the tarball exists else error
    if os.path.exists(tarball_name):
        # Send the tarball file in the response
        return send_file(tarball_name, as_attachment=True)
    else:
        error_message = f"Tarball '{tarball_name}' not found"
        return jsonify({"error": error_message}), 404


def scaffold_collection(collection_name, path="/tmp/"):
    # Execute ansible-creator command to initialize the collection
    try:
        subprocess.run(
            [
                "ansible-creator",
                "init",
                collection_name,
                "--init-path",
                path + str(collection_name.split(".")[0]),
                "--force",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        error_message = (
            f"Failed to initialize Ansible collection '{collection_name}': {e}"
        )
        return jsonify({"error": error_message}), 500


def create_tarball(collection_name, tarball_name, path="/tmp/"):
    # Compress the initialized collection into a tarball
    try:
        subprocess.run(
            ["tar", "-czf", tarball_name, path + str(collection_name.split(".")[0])],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to compress Ansible collection '{collection_name}' into tarball: {e}"
        return jsonify({"error": error_message}), 500


def remove_scaffolded_collection(collection_name, path="/tmp/"):
    # Remove the directory of the initialized collection
    try:
        subprocess.run(
            ["rm", "-rf", path + str(collection_name.split(".")[0])], check=True
        )
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to remove directory '{collection_name}': {e}"
        return jsonify({"error": error_message}), 500


if __name__ == "__main__":
    app.run(debug=True)
