from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Img


# Create your views here.
def upload(request):
    if request.method == 'POST':
        a = Img()
        a.name = request.POST.get('name')
        a.myimage = request.FILES['myimage']
        a.save()
        return HttpResponse('success')
    return render(request, 'img.html')


def show_image(request):
    get_image = Img.objects.all()
    context={'get_image':get_image}
    return render(request, 'showimage.html', {'image': get_image})
