from django.urls import path
from .import views

urlpatterns = [
    path('', views.main),
    path('ways', views.ways)
]