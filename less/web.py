import web

def application(urls, env):
  '''
  A magic less web.py application sample
  
  def hello(ctx, name):
  	if not name:
  		name = 'World'
  	return 'Hello, ' + name + '!'
  	
  urls = ('GET', '/(.*)', hello)
  app = application(urls, locals())
  '''	
  url_list = []
  for method, pattern, handler in urls:
    class Handler:
      pass
    
    def wrap(_handler):
      def wrapped(self, *args, **kwargs):
        return _handler(web.ctx, *args, **kwargs)
      return wrapped
    
    View.__dict__[view.__name__] = wrap(view)
    env[view.__name__] = View
    url_list += [pattern, view.__name__]
  
  def hook_less():
  	''' 
  	Magic Masking Magic Method
  	
  	Lets you write:
  	
  	import web
  	
  	class index:
  		def GET(self):
  			web.header('Content-Type', 'text/html; charset=utf-8', unique=True)
  			web.setcookie('age')
  			web.cookies.get('age')
  			web.input(myfile=None)
  			
  	Without magic as
  	'''
    if web.config.get('session'): web.ctx.session = web.config.session
    web.ctx.setcookie = web.setcookie
    web.ctx.cookies = web.cookies
    web.ctx.input = web.input
    web.ctx.header = web.header
    web.ctx.data = web.data
  
  app = web.application(url_list, env)  
  app.add_processor(web.loadhook(hook_less))
  return app 
