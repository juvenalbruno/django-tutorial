from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt import views


@extend_schema(tags=["auth"])
class TokenObtainPairView(views.TokenObtainPairView):
    ...


@extend_schema(tags=["auth"])
class TokenRefreshView(views.TokenRefreshView):
    ...