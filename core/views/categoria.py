from rest_framework.viewsets import ModelViewSet

from core.models import Categorias
from core.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer