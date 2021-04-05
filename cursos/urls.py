from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import CursoAPIView, AvaliacaoAPIView, AvaliacoesAPIView, CursosAPIView, CursoViewSet,AvaliacaoViewSet

# registrado as rotas de acesso as viewSets criadas
# SimpleRouter só vai gerar as operações CRUDs comuns de um único módulo
# Logo não é possível acessar http://127.0.0.1:8000/api/v2/cursos/1/avaliacoes
router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    # não foi colocado curso_pk pois não iremos sobrescrever nenhum método dessa parte
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),

    # rota que vai pegar um curso e trazer todas as avaliações daquele curso
    # curso_pk é só par asaber que o id é do curso e não da avaliação
    path('cursos/<int:curso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    # rota que vai pegar um curso e trazer todas as avaliações daquele curso
    # curso_pk é só par asaber que o id é do curso e não da avaliação
    # e depois uma avaliação específica daquele curso selecionado
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),


    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao')
]