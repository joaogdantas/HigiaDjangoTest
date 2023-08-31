from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from higiapostquiz.api.views import ContentCategoryViewSet, PostViewSet, QuestionViewSet

router = SimpleRouter()

router.register("categories", ContentCategoryViewSet, basename="categories")
router.register("posts", PostViewSet, basename="posts")
router.register("questions", QuestionViewSet, basename="questions")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+router.urls
