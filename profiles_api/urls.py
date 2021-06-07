from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('helloviewsets', views.HelloViewSets, base_name = 'hello-viewset')
router.register('profile', views.UserProfileViewSets)


urlpatterns = [
    path('helloview/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
