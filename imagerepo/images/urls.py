from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('<int:picture_id>/details', views.details, name='details'),
]