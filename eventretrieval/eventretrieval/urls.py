from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Admin URL
    path('admin/', admin.site.urls),

    # URL to include the events app
    path('search', include('events.urls')),
]