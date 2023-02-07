
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import PostViewSet

router = DefaultRouter()
router.register('Post',PostViewSet, 'Post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
