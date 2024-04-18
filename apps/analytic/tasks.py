from decimal import Decimal

from django.db import transaction
from django.db.models import Avg, Count, Sum

from apps.analytic.models import CategoryAnalyticModel, PlaceAnalyticModel
from apps.check.models import CheckModel
from apps.product.models import ProductModel
from config.celery import app
from config.settings.base import REDIS_CONNECTION


@app.task
def analytic_calculate():
    """Периодический расчет аналитики по времени"""
    last_check_id = REDIS_CONNECTION.get('last_check_id')
    if last_check_id is None:
        last_check_id = 0
    else:
        last_check_id = int(last_check_id)
    place_analytics = (
        CheckModel.objects.filter(id__gt=last_check_id)
        .values('id', 'place__id', 'place__name')
        .annotate(
            total_purchases=Count('id'),
            average_receipt=Avg('total_amount'),
            taxes_amount=Sum('nds_amount') + Sum('tips_amount'),
            total_nds=Sum('nds_amount'),
            total_tips=Sum('tips_amount'),
        )
    )

    if place_analytics.exists():
        last_analyzed_check_id = place_analytics.latest('id').get('id')
        REDIS_CONNECTION.set('last_check_id', last_analyzed_check_id)

    category_analytics = ProductModel.objects.values('category__name').annotate(
        total_spent=Sum('price'), average_receipt=Avg('price')
    )
    with transaction.atomic():
        for place_data in place_analytics:
            place = PlaceAnalyticModel.objects.filter(place_name=place_data['place__name']).first()

            if place:
                place.place_id = place_data['place__id']
                place.place_name = place_data['place__name']
                place.total_purchases = place.total_purchases + place_data['total_purchases']
                place.average_receipt = Decimal(place.average_receipt) + Decimal(place_data['average_receipt'])
                place.taxes_amount = place.taxes_amount + Decimal(place_data['taxes_amount'])
                place.total_nds = place.total_nds + Decimal(place_data['total_nds'])
                place.total_tips = place.total_tips + Decimal(place_data['total_tips'])
                place.save()

            else:
                PlaceAnalyticModel.objects.create(
                    place_id=place_data['place__id'],
                    place_name=place_data['place__name'],
                    total_purchases=place_data['total_purchases'],
                    average_receipt=place_data['average_receipt'],
                    taxes_amount=place_data['taxes_amount'],
                    total_nds=place_data['total_nds'],
                    total_tips=place_data['total_tips'],
                )

        for category_data in category_analytics:
            category = CategoryAnalyticModel.objects.filter(name=category_data['category__name']).first()
            if category:
                category.name = category_data['category__name']
                category.total_spent = category.total_spent + category_data['total_spent']
                category.average_receipt = category.average_receipt + category_data['average_receipt']
                category.save()
            else:
                CategoryAnalyticModel.objects.create(
                    name=category_data['category__name'],
                    total_spent=category_data['total_spent'],
                    average_receipt=category_data['average_receipt'],
                )
