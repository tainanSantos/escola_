from rest_framework import generics
from rest_framework.generics import get_object_or_404

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

    # sobrescrevendo método get_queryset
    # o metodo get_queryset retorna uam lista
    # pegando todas as avaliações de um determinado curso
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):  # self.kwargs.get('curso_pk') verificando se veio algum curso_pk na url

            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))  # retornando todas as avaliaçõe do curso
        return self.queryset.all()  # retornando todas as avaliações


# buscar um, editar um e deletar um
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # o método get_object retorna uma lista
    # pegando uam avaliação específica do curso selecionado
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
