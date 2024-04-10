# container-ansible-creator

Builds a container with ansible creator to scaffold a collection within it and exposes a POST API to download a tarball of the collection

```bash
 podman build -t my_creator_image .
 podman run -p 3100:5000 my_creator_image
 curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"collection_name": "myapp.test"}' \
  http://localhost:3100/fetch_collection_tar --output collection.tgz
```
