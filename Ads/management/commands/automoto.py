from django.core.management import BaseCommand
from Ads.automoto import scrape_single_ad
from Ads.models import Ads, MainImage, Image
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            ad_info = scrape_single_ad(soup, url) 

            if ad_info:
                image_urls = ad_info["image_urls"]
                del ad_info["image_urls"]

                image_instances = []
                for image_url in image_urls:
                    image_instance, created = Image.objects.get_or_create(image=image_url)
                    image_instances.append(image_instance)

                main_image_url = ad_info.pop("image", None)
                if main_image_url:
                    main_image, created = MainImage.objects.get_or_create(image=main_image_url)
                    ad_info["main_image"] = main_image

                ad_instance = Ads.objects.create(**ad_info)
                ad_instance.images.set(image_instances)

                self.stdout.write(self.style.SUCCESS('succes'))
            else:
                self.stdout.write(self.style.ERROR('failed'))