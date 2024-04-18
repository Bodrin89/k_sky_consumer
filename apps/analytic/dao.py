from django.db.models import Sum

from apps.analytic.models import CategoryAnalyticModel, PlaceAnalyticModel
from apps.check.models import CheckModel


class AnalyticDAO:
    @staticmethod
    def get_analytic_places():
        return PlaceAnalyticModel.objects.all()

    @staticmethod
    def get_analytic_categories():
        return CategoryAnalyticModel.objects.all()

    @staticmethod
    def get_delta_times(start_date, end_date):
        return CheckModel.objects.filter(timestamp__range=[start_date, end_date]).aggregate(Sum('tips_amount'))
