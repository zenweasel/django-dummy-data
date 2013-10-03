
from django.template.response import TemplateResponse


def direct_to_template(request):
    return TemplateResponse(request, 'home.html', status=404)


def login(request):
    post_vars = request.POST
    if post_vars.get('username') != 'parkme' or post_vars.get('password') != 'parkme':
        return TemplateResponse(request, 'fail.html', status=401)
    else:
        return TemplateResponse(request, 'success.html', status=401)

