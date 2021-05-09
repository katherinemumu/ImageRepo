from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .form import ImageForm
from .models import Image
from datetime import datetime

def index(request):
    template = loader.get_template('images/index.html')
    pics = Image.objects.all()
    print('++++++++++++++++++' + str(type(pics)) + "+++++ " + str(pics))
    length = len(pics)
    i = 0
    array = []
    sub_array =[]
    for pic in pics:
        img_path = "../../../media/" + str(pic.image)
        print(img_path)
        sub_array.append(img_path)
        if len(sub_array) == 3:
            array.append(sub_array)
            sub_array = []
    if len(sub_array) < 3:
        array.append(sub_array)
    print(array)
    return render(request, 'images/index.html', {'array': array})
    # "../../../media/pusheeen.jpg"


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

