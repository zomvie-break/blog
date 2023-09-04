from rest_framework import serializers
from .models import Weight

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = [
            'user',
            'mass',
            'created',
        ]