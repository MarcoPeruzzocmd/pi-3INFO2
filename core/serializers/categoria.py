from rest_framework.serializers import ModelSerializer

from core.models import Categorias

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"