from apps.models import SingerModel, SongModel
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields = ['id', 'title', 'singer']

class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True, read_only=True)

    class Meta:
        model = SingerModel
        fields = ['id', 'name', 'age', 'country', 'song', ]

