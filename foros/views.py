from .models import Usuario, Foro, Comentario, Categoria, ClasificacionForo
from .serializers import UsuarioSerializer, ForoSerializer, ComentarioSerializer, CategoriaSerializer, ClasificacionForoSerializer
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import generics


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ForoList(generics.ListCreateAPIView):
    queryset = Foro.objects.all()
    serializer_class = ForoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id_creador', 'titulo']

class ForoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foro.objects.all()
    serializer_class = ForoSerializer

class ComentarioList(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClasificacionForoList(generics.ListCreateAPIView):
    queryset = ClasificacionForo.objects.all()
    serializer_class = ClasificacionForoSerializer

class ClasificacionForoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClasificacionForo.objects.all()
    serializer_class = ClasificacionForoSerializer

