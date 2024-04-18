from rest_framework import serializers

from apps.store.models import StoreModel


class GetAllPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = ('id', 'name')
