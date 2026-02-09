from django.urls import path
from .views import EquipoListAPIView, EquipoDetailAPIView

urlpatterns = [
    path('equipos/', EquipoListAPIView.as_view(), name='equipo-list'),
    path('equipos/<int:pk>/', EquipoDetailAPIView.as_view(), name='equipo-detail'),
]