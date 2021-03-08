from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajaxSave', views.save, name='save'),
]