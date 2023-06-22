from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("restaurant/<int:pk>", views.full_details, name='full_details')
]
