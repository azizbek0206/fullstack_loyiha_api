from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Sizning app'ingizdagi views faylidan import qiling
from products.views import ProductViewSet


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Inventarizatsiya API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # API yo'nalishlarini qo'shish
    path('', include('products.urls')), # API yo'nalishlarini qo'shish


    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]