from django.template.response import TemplateResponse


def see_quacks(request):
    return TemplateResponse(request, 'request_response/see_quacks.html')
