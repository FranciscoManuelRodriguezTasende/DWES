import django_filters
from .models import Equipo

class EquipoFilter(django_filters.FilterSet):
    # Filtro avanzado: Rango de años de fundación
    desde_anio = django_filters.NumberFilter(field_name="fundacion", lookup_expr="gte")
    hasta_anio = django_filters.NumberFilter(field_name="fundacion", lookup_expr="lte")

    class Meta:
        model = Equipo
        fields = ['activo', 'ciudad'] # Filtros simples