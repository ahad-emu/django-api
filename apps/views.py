from apps.models import SingerModel, SongModel
from django.shortcuts import render
from rest_framework import viewsets
from apps.serializers import SingerSerializer, SongSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class SingerModelView(viewsets.ModelViewSet):
    queryset = SingerModel.objects.all()
    serializer_class = SingerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class SongModelView(viewsets.ModelViewSet):
    queryset = SongModel.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]