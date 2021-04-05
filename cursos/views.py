from rest_framework.views import APIView
from rest_framework.response import Response
# status de respostas da api
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de Curso da Geek
    """

    def get(self, request):
        print("INFORMAÇÕES DO REQUEST")
        print(dir(request))
        print(request.query_params)
        print(request.user)

        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        # se os dados forem inválidos ele já para aqui e lança uma exception
        serializer.is_valid(raise_exception=True)
        serializer.save() # salvando do dados no BD
        return Response(serializer.data, status =status.HTTP_201_CREATED)
        # return Response({"id":serializer.data['id'], "curso":serializer.data['titulo']}, status =status.HTTP_201_CREATED)
        # return Response({"msg":"Curso criado com sucesso"}, status =status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    """
    Api de Avaliações da Geek
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        # many=True quer dizer qu eeu quero buscar todas as avaliações
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        # se os dados forem inválidos ele já para aqui e lança uma exception
        serializer.is_valid(raise_exception=True)
        serializer.save() # salvando do dados no BD
        return Response(serializer.data, status =status.HTTP_201_CREATED)

