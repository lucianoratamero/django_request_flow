

def add_a_quack(request):
    context = {}
    context['quackalicious'] = 'quacking from the context processor!'
    return context
