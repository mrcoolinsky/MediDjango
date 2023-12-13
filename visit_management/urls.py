from django.urls import path
from .views import visit_list, make_appointment
urlpatterns = [
    path('visit-list/', visit_list, name='visit_list'),
    path('make-appointment/', make_appointment, name='make_appointment'),
]
