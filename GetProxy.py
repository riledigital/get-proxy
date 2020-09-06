# things.py

# Let's get this party started!
import falcon
import json

from pathlib import Path

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.


class ProxyResource(object):
    _CHUNK_SIZE_BYTES = 4096

    def load_txt(self, file_path):
        # li = []
        return [line.rstrip('\n') for line in open(file_path, mode='r', newline='')]

    def __init__(self):
        self.PROXIES_LIST = self.load_txt(Path('inlist.txt'))

    def on_post(self, req, resp):
        print(req)
        print(list(self.PROXIES_LIST))
        # proxylist = json.loads(req.stream.read())
        chunk = req.stream.read(self._CHUNK_SIZE_BYTES)
        removedproxylist = json.loads(chunk)['remove']
        removed = filter(lambda x: x not in removedproxylist, self.PROXIES_LIST)
        self.PROXIES_LIST = list(removed)
        print(self.PROXIES_LIST)
        resp.body = "Yo Removed some proxies~"
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        # Retrieve and send back a thing
        # resp.body = (f'{self.PROXIES_LIST}')
        resp.body = json.dumps({'proxies': self.PROXIES_LIST}, ensure_ascii=False)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
proxyResource = ProxyResource()

# things will handle all requests to the '/things' URL path
app.add_route('/proxies', proxyResource)

# Useful for debugging problems in your API; works with pdb.set_trace(). You
# can also use Gunicorn to host your app. Gunicorn can be configured to
# auto-restart workers when it detects a code change, and it also works
# with pdb.
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8009, app)
    httpd.serve_forever()