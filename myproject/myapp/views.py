from django.shortcuts import render, get_object_or_404
from .models import MyObject

def feed(request):
    objects = MyObject.objects.all()
    return render(request, 'index.html', {'objects': objects})

def detail(request, object_id):
    object = get_object_or_404(MyObject, id=object_id)
    return render(request, 'detail.html', {'object': object})
