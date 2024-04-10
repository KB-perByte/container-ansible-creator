# container-ansible-creator

Builds a container with ansible creator and scaffolds a collection within it and exposes a POST API to download a tarball of the same

```bash
 podman build -t my_creator_image .
 podman run -p 3100:5000 my_creator_image
 curl -X POST \\n -H "Content-Type: application/json" \\n -d '{"collection_name": "myapp.test"}' \\n http://localhost:3100/generate_collection --output .
```
