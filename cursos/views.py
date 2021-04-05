from rest_framework import generics
from rest_framework.response import Response
# status de respostas da api
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


# class CursoAPIView(generics.ListCreateAPIView):
#     queryset = Curso.objects.all()
#     serializer_class = CursoSerializer
#
#
# class AvaliacaoAPIView(generics.ListCreateAPIView):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer


# criar e buscar todos
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# buscar um, editar um e deletar um
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# criar e buscar todos
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

# buscar um, editar um e deletar um
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
