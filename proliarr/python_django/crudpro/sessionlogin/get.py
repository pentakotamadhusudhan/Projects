from django.http import HttpResponse


def time(request):
    request.session.set_expiry(20)
    if 'name' in request.session:
        return HttpResponse('login success')
    else:
        return HttpResponse('session expiry')
