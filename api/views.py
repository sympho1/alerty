from django.shortcuts import render
from api.models import Alert, Author, Alerter, Victim, Abus
from api.serializers import AlerterSerializer, AlertSerializer, AuthorSerializer, VictimSerializer, AbusSerializer
from rest_framework.viewsets import ModelViewSet


class AlerterViewSet(ModelViewSet):
    queryset = Alerter.objects.all()
    serializer_class = AlerterSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class VictimViewSet(ModelViewSet):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializer


class AlertViewSet(ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    pass


class AbusViewSet(ModelViewSet):
    queryset = Abus.objects.all()
    serializer_class = AbusSerializer
    pass

# Create your views here.
