import os

from django.db import IntegrityError, transaction
from dotenv import load_dotenv
from kafka.consumer import KafkaConsumer

from apps.check.models import CheckModel
from apps.product.models import CategoryModel, ProductModel
from apps.store.models import StoreModel
from config.settings.base import LOGGER
from schemas.checks_schema import CheckSchema

load_dotenv()


def kafka_consumer():
    """Прием сообщений из кафки и запись в базу данных"""
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
    consumer = KafkaConsumer('send_checks', bootstrap_servers=bootstrap_servers)
    consumer.subscribe(topics=['send_checks'])
    print('Listening for messages...')
    for message in consumer:
        check_schema = CheckSchema.parse_raw(message.value.decode('utf-8'))

        try:
            with transaction.atomic():
                place_name = 'another_name'
                if check_schema.place_name:
                    place_name = check_schema.place_name
                place, _ = StoreModel.objects.get_or_create(name=place_name)
                check = CheckModel.objects.create(
                    transaction_id=check_schema.transaction_id,
                    timestamp=check_schema.timestamp,
                    total_amount=check_schema.total_amount,
                    nds_amount=check_schema.nds_amount,
                    tips_amount=check_schema.tips_amount,
                    payment_method=check_schema.payment_method,
                    place=place,
                )

                for item in check_schema.items:
                    category, _ = CategoryModel.objects.get_or_create(name=item.category)

                    ProductModel.objects.create(
                        product_id=item.product_id,
                        check_transaction=check,
                        quantity=item.quantity,
                        price=item.price,
                        category=category,
                    )

        except IntegrityError as e:
            LOGGER.error(e)
