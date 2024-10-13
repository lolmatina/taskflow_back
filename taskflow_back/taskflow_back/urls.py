from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
]


schema_view = get_schema_view(
    openapi.Info(
        title="TaskFlow API",
        default_version='v1',
        description="API documentation for TaskFlow project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@taskflow.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
