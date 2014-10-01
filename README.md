less.web.py -- web.py without mits of magic.
===========

A tiny wrapper around web.py's request handling. 

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

```
def hello(ctx):
	user_data = ctx.input(color=[])
	if 'color' not in ctx.cookies and not user_data.color:
		ctx.setcookies('color', 'blue')
	return 'Hello, from ' + ctx.env.get('REMOTE_HOST') or ctx['ip'] 
urls = ('GET', '/', hello)
import less.web
app = less.web.application(urls, locals())
```

```python

def redirect_to_referer(ctx):
	referer = ctx.env.get('HTTP_REFERER', 'http://webpy.org')
	raise web.seeother(referer) 

```	
