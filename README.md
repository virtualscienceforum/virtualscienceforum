# Virtual Science Forum

This repository hosts all the files for https://virtualscienceforum.org.

See [assets](assets.md) for the listing of other resources we use.

## Testing changes locally

If you want to test changes to the markdown content locally, you can simply run
python's http.server in the root directory of your copy of this repository.

```
cd /root/of/virtualscienceforum
python3 -m http.server
```

This starts a simple http server on port 8000 on your local machine
that will serve the content. In other words, point your browser to localhost:8000.

http.server takes as optional argument a port number in case you want to use a
different port (e.g. when issuing `python3 -m http.server 8888` the server
will listen on port 8888 and thus the content is served at localhost:8888). 
