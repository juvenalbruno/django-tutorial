from django.contrib import admin
from django.urls import path, include

prefix = 'api'

urlpatterns = [
    path(f'{prefix}/auth/', include('core.authentication.urls')),
    path(f'{prefix}/docs/', include('server.docs.urls')),
]
