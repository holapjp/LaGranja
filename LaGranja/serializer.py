from rest_framework import serializers
from .models import Porcino
from .models import Alimentacion
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
  

class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacion
        fields = "__all__"


class PorcinoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    alimentacion = AlimentacionSerializer(read_only=True)

    clienteId = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), write_only=True, source='cliente')
    alimentacionId = serializers.PrimaryKeyRelatedField(queryset=Alimentacion.objects.all(), write_only=True, source='alimentacion')


    class Meta:
        model = Porcino
        fields = "__all__"




    

