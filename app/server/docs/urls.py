from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(),
         {
             'GET': 'Recuperação do schema da API',
         },
         name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'),
         {
             'GET': 'Recuperação da documentação da API',
         },
         name='swagger-ui'),

]
