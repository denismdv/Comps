from django.urls import path, include
from rest_framework import routers, permissions
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
openapi.Info(
    title="Swagger",
    default_version='v1',
    description="...",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="hello@mycompany.com"),
    license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('comps', CompsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
]