from django.urls import path
from . import views

urlpatterns = [

    path('visits', views.visits, name="visits"),
    path('visit/edit/<int:visit_id>/', views.visit_edit, name="visit_edit"),
    path('visit/edit/add', views.visits, name="visit_add"),
    path('visit/edit/change', views.visits, name="visit_change"),
    path('visit/edit/delete', views.visits, name="visit_delete"),
    path('visit/view/<int:visit_id>/', views.view_visit, name="view_visit"),

]