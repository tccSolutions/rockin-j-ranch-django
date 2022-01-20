from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>/<str:pk>", views.horse, name="horse"),
    path("add-image/<str:pk>", views.add_image, name="add-image"),
     path("delete-image/", views.delete_image, name="delete-image"),
]