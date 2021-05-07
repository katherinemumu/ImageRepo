from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .form import ImageForm
from datetime import datetime

def index(request):
    template = loader.get_template('images/index.html')
    return HttpResponse(template.render({}, request))

def upload(request):
    if request.method == 'POST':
        print('////////////////////////// in post if')
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_object = form.instance 
            print('image.url://////////////' + image_object.image.url)
            return render(request, 'images/upload.html', {'form': form, 'image_object': image_object})
    else:
        print('////////////////////in else IN GET NOT POST')
        form = ImageForm()
    return render(request, 'images/upload.html', {'form': form})
    '''
    template = loader.get_template('images/upload.html')
    return HttpResponse(template.render({}, request))
    '''

def details(request, picture_id):
    return HttpResponse("This is where you can view the picture for id " + str(picture_id) + " on the big screen and see the tags/other details")

