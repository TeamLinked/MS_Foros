from foros import views
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view()),
    path('usuarios/<int:pk>', views.UsuarioDetail.as_view()),
    path('foros/', views.ForoList.as_view()),
    path('foros/<int:pk>', views.ForoDetail.as_view()),
    path('comentarios/', views.ComentarioList.as_view()),
    path('comentarios/<int:pk>', views.ComentarioDetail.as_view()),
    path('categorias/', views.CategoriaList.as_view()),
    path('categorias/<int:pk>', views.CategoriaDetail.as_view()),
    path('clasificacionforos/', views.ClasificacionForoList.as_view()),
    path('clasificacionforos/<int:pk>', views.ClasificacionForoDetail.as_view()),
    path('', include(router.urls)),
]


