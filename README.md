# container-ansible-creator

10327 podman build -t my_creator_image .
10328 podman run -p 3100:5000 my_creator_image
10330 curl -X POST \\n -H "Content-Type: application/json" \\n -d '{"collection_name": "myapp.test"}' \\n http://localhost:3100/generate_collection --output .
