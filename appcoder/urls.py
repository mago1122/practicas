from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("", inicio),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("cursos/re-locos", cursos, name="coder-cursos"),
    path("entregables/", entregables, name="coder-entregables")
]