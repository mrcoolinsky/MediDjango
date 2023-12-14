from django.urls import path
from . import views

urlpatterns = [

    path('documentation', views.documentation, name="documentation"),
    path('documentation/view/<int:patient_id>/', views.view_documentation, name="view_documentation"),

]