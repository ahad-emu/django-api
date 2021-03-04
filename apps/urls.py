from django.urls import path, include
from apps import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singer', views.SingerModelView, basename='singer')
router.register('song', views.SongModelView, basename='song')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
