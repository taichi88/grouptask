from rest_framework import serializers
from .models import Car



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year_model', 'price', 'slug']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user = self.context.get('request').user

        if not user.is_authenticated:
            representation.pop('slug', None)

        return representation


