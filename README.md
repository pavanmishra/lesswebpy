Simplified web.py.
===========

Making `web.py` request handling more pythonic.


```python

import less.web

def hello(ctx, name):
  if not name:
    name = 'World'
  return 'Hello, ' + name + '!'

urls = ('GET', '/(.*)', hello)

app = less.web.application(urls, locals())

```

All those magical web.* are now available in context variable.

```python

def hello(ctx):
  user_data = ctx.input(color=[])
  if 'color' not in ctx.cookies and not user_data.color:
    ctx.setcookies('color', 'blue')
  return 'Hello, from ' + ctx.env.get('REMOTE_HOST') or ctx.ip

urls = ('GET', '/', hello)
import less.web
app = less.web.application(urls, locals())

```

Only a part of web.py request handling has been masked with `less.web`. Rest of them are required to
do what they did already.

```python
import web
import less.web

def redirect_to_referer(ctx):
	referer = ctx.env.get('HTTP_REFERER', 'http://webpy.org')
	raise web.seeother(referer)

urls = ('GET', '/', redirect_to_referer)
app = less.web.application(urls, locals())
```
It's implemented as a tiny pythonic wrapper around `web.py` request handling.

The idea is to allow all request/response manipulation through `ctx`(context) of the handler function rather than module(`web`) level functions. `ctx` is basically `web.ctx` of `web.py`, which is already used to set and access request context. It also wraps other module level functionality of `web.py` such as `header`, `input`, `cookies`, `sessions` to yield a more pythonic interface.

To use sessions you have to configure session store in config as follows.

```python
web.config.sessionstore = web.session.DiskStore('sessions') # for disk store, other stores can be used similarly.
```
