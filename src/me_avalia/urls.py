from django.urls import include, path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app import views, admin

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="ME AVALIA API",
      default_version='v1',
      description="Projeto Desenvolvimento de Sistemas Web - UNEMAT",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('admin/', admin.admin.site.urls),
   path('aluno', views.StudentRetrieve.as_view()),
   path('avaliacao', views.RatingPostViewSet.as_view(), name='avaliavao'),
   path('avaliacao/<uuid:pk>', views.RatingUpdateView.as_view(), name="avaliacao"),
   path('show_avaliacao/<uuid:pk>', views.RatingGetViewset.as_view()),
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]







