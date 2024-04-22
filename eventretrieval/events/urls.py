from django.urls import path
from . import views

urlpatterns = [

    # URL pattern to retrieve events
    path('', views.get_events, name='get_events'),
]