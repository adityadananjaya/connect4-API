from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import GameView, UpdateView, MinmaxResponse

game_router = DefaultRouter()
game_router.register(r'update', UpdateView)
game_router.register(r'minmax', MinmaxResponse)