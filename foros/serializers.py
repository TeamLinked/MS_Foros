from rest_framework import serializers
from .models import Usuario, Foro, Comentario, Categoria, ClasificacionForo


class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = '__all__'
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class ComentarioSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comentario
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Categoria
        fields = '__all__'

class ClasificacionForoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = ClasificacionForo
        fields = '__all__'