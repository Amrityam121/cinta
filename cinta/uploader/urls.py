from django.urls import path

from . import views

urlpatterns = [
    # path('upload', views.uploader_index, name='uploader_index'),
    path('myupload', views.Myuploader_index, name='Myuploader_index'),
    path('delete/<int:id>', views.destroy_photo, name='destroy_photo'),
]