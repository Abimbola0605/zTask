from rest_framework import serializer
from.models import link

class LinkSerializer(serializer.ModelSerializer):
    class Meta:
        model = link
        fields = "__all__"