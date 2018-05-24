
import django
from django.core.handlers.wsgi import WSGIHandler


class CustomWSGIHandler(WSGIHandler):

    def __init__(self, *args, **kwargs):
        django.setup(set_prefix=False)
        super().__init__(*args, **kwargs)

    def __call__(self, environ, start_response):
        environ['HTTP_COOKIE'] = environ['HTTP_COOKIE'] + '; quackfrombeyond="quack from the wsgi app!"'
        return super().__call__(environ, start_response)


application = CustomWSGIHandler()
