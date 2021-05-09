from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .form import ImageForm
from .models import Image
from datetime import datetime

def index(request):
    template = loader.get_template('images/index.html')
    pics = Image.objects.all()
    length = len(pics)
    i = 0
    array = []
    sub_array =[]
    for pic in pics:
        img_path = "../../../media/" + str(pic.image)
        sub_array.append(img_path)
        if len(sub_array) == 3:
            array.append(sub_array)
            sub_array = []
    if len(sub_array) < 3:
        array.append(sub_array)
    return render(request, 'images/index.html', {'array': array})

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_object = form.instance
            return render(request, 'images/upload.html', {'form': form, 'image_object': image_object})
    else:
        form = ImageForm()
    return render(request, 'images/upload.html', {'form': form})

def details(request, picture_id):
    return HttpResponse("This is where you can view the picture for id " + str(picture_id) + " on the big screen and see the tags/other details")

