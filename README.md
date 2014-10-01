less.web.py -- web.py without mits of magic.
===========

A tiny pythonic wrapper around web.py's request handling.

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
		return 'Hello, from ' + ctx.env.get('REMOTE_HOST') or ctx.ip 
	
	urls = ('GET', '/', hello)
	import less.web
	app = less.web.application(urls, locals())

```python

Only a part of web.py request handling has been masked with `less.web`. Rest of them are required to 
do what they already did.

```python
	import web
	import less.web

	def redirect_to_referer(ctx):
		referer = ctx.env.get('HTTP_REFERER', 'http://webpy.org')
		raise web.seeother(referer) 

	urls = ('GET', '/', redirect_to_referer)
	app = less.web.application(urls, locals())
```	
