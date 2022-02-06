from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>/<str:pk>", views.horse, name="horse"),
    path("add-image", views.add_image, name="add-image"),
    path("delete-image/", views.delete_image, name="delete-image"),
    path("request_info", views.request_info, name='request-info'),
    path("training_notes/<str:pk>/", views.notes, name="notes"),
]