from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="FinSure API", default_version="v1"),
    public=True, permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/transactions/", include("transactions.urls")),
    path("api/budget/", include("budget.urls")),
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api-docs"),
]
