from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from django.urls import path, re_path, include
from api.views import AlerterViewSet, AbusViewSet, AuthorViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register("alerters", AlerterViewSet)
router.register("abus", AbusViewSet)
router.register("authors", AuthorViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Infants Abuse API",
        default_version="v1",
        description="Test Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]