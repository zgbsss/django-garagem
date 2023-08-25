from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo
from garagem.serializers import (AcessorioSerializer, CategoriaSerializer,
                                 CorSerializer, MarcaSerializer,
                                 ModeloSerializer, VeiculoDetailSerializer,
                                 VeiculoListSerializer, VeiculoSerializer)
