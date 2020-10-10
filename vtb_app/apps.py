from django.apps import AppConfig
from json import dump
from .vtb_api import get_marketplace_data


class VtbAppConfig(AppConfig):
    name = 'vtb_app'

    # Preload marketplace data once the app is ready
    def ready(self):
        with open("marketplace.json", "w") as file:
            dump(get_marketplace_data(), file, ensure_ascii=False)
        
