from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-nearest-location', views.nearest_location, name="nearest_location"),
]
