from pip._vendor.distro import version
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

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

"""
API V1
"""


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


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # aqui estamos criando um naova rota para avaliações
    # e trazendo todas as avaliações do curso selecioando
    # detail=True, é para que ele crie a rota de avaliações
    # methods=['get'] corresponde por qul tipo de método que este recuros pode ser acessado
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):

        # temos que colocar aqui a paginaçaõ de forma manual
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        curso = self.get_object()  # pegando o curso selcionado
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

# faz a mesma coisa da class comentada acima
# o que muda é que se desejar excluir algum método do crud
# é so excluir uma atribito de mixins
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
