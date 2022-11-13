from django.urls import path, include
from rest_framework import routers

from poker.views import GameSessionView

router = routers.DefaultRouter()
router.register("sessions", GameSessionView)
urlpatterns = [
    path("", include(router.urls))
]

app_name = "poker"
