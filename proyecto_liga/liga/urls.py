from django.urls import path
from .views import EquipoListAPIView, EquipoDetailAPIView

urlpatterns = [
    path('equipos/', EquipoListAPIView.as_view()),      # GET (lista) y POST (crear)
    path('equipos/<int:pk>/', EquipoDetailAPIView.as_view()), # GET (detalle)
]