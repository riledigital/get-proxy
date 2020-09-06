# Simple Rotating Proxy Server

Install dependencies with `pipenv install`

Run it with `gunicorn GetProxy:app`

`GET` request to `/proxies/all` to get a list of all servers

`GET` request to `/proxies/next` to get a single server

`POST` to `/proxies/delete` to delete a dead proxy
