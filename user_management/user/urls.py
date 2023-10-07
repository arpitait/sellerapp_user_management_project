from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user1',views.UserView,basename='userr')


urlpatterns = [
    path("1/",include(router.urls)),
]