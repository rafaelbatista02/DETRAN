from rest_framework import serializers
from proprietario.models import Dono

class DonoSerializer(serializers.Serializer):
    nome = serializers.CharField()
    rg = serializers.IntegerField()
    cpf = serializers.IntegerField()
    endereço = serializers.CharField()

    def create(self,validated_data):
        proprietario = Dono.objects.create(**validated_data)
        return proprietario

    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.rg = validated_data.get('rg', instance.rg)
        instance.cpf = validated_data.get('cpf',instance.cpf)
        instance.endereço = validated_data.get('endereço',instance.endereço)
        instance.save()
        return instance 