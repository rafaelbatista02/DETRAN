from django.shortcuts import render
from rest_framework import viewsets
from proprietario.models import Dono
from proprietario.serializers import DonoSerializer

class DonoViewSet(viewsets.ModelViewSet):
    queryset = Dono.objects.all()
    serializer_class = DonoSerializer
