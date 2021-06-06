from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializing an input for our API"""
    name = serializers.CharField(max_length = 10)
