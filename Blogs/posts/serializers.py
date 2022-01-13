from rest_framework import serializers
from .models import *

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class contactserializer(serializers.ModelSerializer):
    class Meta:
        model = contact_us
        fields = "__all__"

class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"