from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('json_img', views.json_img, name='json_img'),

]
 