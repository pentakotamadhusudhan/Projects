from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('admin/',parement=True)