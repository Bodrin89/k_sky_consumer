from django.core.management.base import BaseCommand

from apps.consumer.utils import kafka_consumer


class Command(BaseCommand):
    help = 'Starts Kafka consumer'

    def handle(self, *args, **options):
        while True:
            kafka_consumer()
