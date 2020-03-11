from rest_framework import serializers
from .models import Songs, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", )

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")
