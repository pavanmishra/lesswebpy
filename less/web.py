import web

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
      return 'Spelled'

  Without magic as:

  def index(ctx):
    ctx.header('Content-Type', 'text/html; charset=utf-8', unique=True)
    ctx.setcookie('age')
    ctx.cookies.get('age')
    ctx.input(myfile=None)
    return 'Dispelled'
  '''
  if web.config.get('session'): web.ctx.session = web.config.session
  web.ctx.setcookie = web.setcookie
  web.ctx.cookies = web.cookies
  web.ctx.input = web.input
  web.ctx.header = web.header
  web.ctx.data = web.data


def application(urls, env):
  '''
  A magic less web.py application

  def hello(ctx, name):
  	if not name:
  		name = 'World'
  	return 'Hello, ' + name + '!'

  urls = ('GET', '/(.*)', hello)
  app = application(urls, locals())
  '''
  def url_handler_class(method, pattern, handler):
    ''' convert functional view to class based view consumable by rest of webpy '''
    class View:
      pass
    def wrap(_handler):
      def wrapped(self, *args, **kwargs):
        return _handler(web.ctx, *args, **kwargs)
      return wrapped
    View.__dict__[handler.__name__] = wrap(handler)
    env[handler.__name__] = View
    return pattern, handler.__name__
  def urls_to_webpy(urls):
    ''' convert to webpy format '''
    return [url_handler_class(method, pattern, handler) for method, pattern, handler in urls]
  app = web.application(urls_to_webpy(urls), env)
  app.add_processor(web.loadhook(hook_less))
  return app
