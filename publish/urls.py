from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'trainings', views.TrainerViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.home, name='home'),
]
