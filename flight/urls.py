from django.urls import path
from .views import FligtView,ReservationView
from rest_framework import routers


router = routers.DefaultRouter()
router.register("flights",FligtView)
router.register("reservations", ReservationView)
urlpatterns = [


]
urlpatterns += router.urls