from django.urls import path
from . import views

urlpatterns = [

    path('documentation', views.documentation, name="documentation"),

]