from django.apps import AppConfig
from threading import Thread
from kafka import KafkaConsumer

class ConsumerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consumer_app'

    def ready(self) -> None:


        return super().ready()

