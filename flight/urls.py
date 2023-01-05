from django.urls import path
from .views import FligtView
from rest_framework import routers


router = routers.DefaultRouter()
router.register("flights",FligtView)

urlpatterns = [


]
urlpatterns += router.urls