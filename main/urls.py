from django.urls import path
from . import views
from django.urls import include

urlpatterns = [

    path('', views.main, name="main"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('visit-management/', include('visit_management.urls')),

]