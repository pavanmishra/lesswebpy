import lessweb

def index(ctx):
  return 'Hello'

def hello(ctx, name):
  if not name:
    name = 'World'
  return 'Hello, ' + name + '!'

urls = (
  'GET', '/?', index,
  'GET', '/(.*)', hello
)

app = lessweb.application(urls, locals())

if __name__ == '__main__':
  app.run()
