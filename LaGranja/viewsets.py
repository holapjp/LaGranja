from rest_framework import viewsets
from .serializer import *
from .models import *

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PorcinoViewSet(viewsets.ModelViewSet):
    queryset = Porcino.objects.all()
    serializer_class = PorcinoSerializer


class AlimentacionViewSet(viewsets.ModelViewSet):
    queryset = Alimentacion.objects.all()
    serializer_class = AlimentacionSerializer
