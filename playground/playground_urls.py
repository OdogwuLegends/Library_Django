from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.playground),
    path('show_name/', views.show_my_name)
]
