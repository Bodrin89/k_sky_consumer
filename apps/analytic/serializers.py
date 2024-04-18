from rest_framework import serializers

from apps.analytic.models import CategoryAnalyticModel, PlaceAnalyticModel


class GetAnalyticPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceAnalyticModel
        fields = (
            'id',
            'place_id',
            'place_name',
            'total_purchases',
            'average_receipt',
            'taxes_amount',
            'total_nds',
            'total_tips',
        )


class GetAnalyticCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAnalyticModel
        fields = (
            'id',
            'name',
            'total_spent',
            'average_receipt',
        )


class GetAnalyticDeltaTimeSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
