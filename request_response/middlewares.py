

class DuckMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.COOKIES['quacks'] = ['quack from the cookies!']
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        context = response.context_data or {}
        quacks = context.get('quacks', [])

        if request.COOKIES.get('quackfrombeyond'):
            quacks.append(request.COOKIES.get('quackfrombeyond'))

        quacks.append('quack from the middleware!')

        if request.COOKIES.get('quacks'):
            quacks = quacks + request.COOKIES['quacks']

        context['quacks'] = quacks
        response.context_data = context
        return response
