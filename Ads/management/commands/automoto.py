from django.core.management import BaseCommand
from Ads.automoto import load_json
from Ads.models import Ads, MainImage , Image

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = load_json()
        data = list(data)
        for ad in data:
            
            image_url = ad['image']
            image, created = MainImage.objects.get_or_create(image=image_url)
            
            ad = Ads.objects.create(
                title=ad["title"],
                price=ad["price"],
                year=ad["year"],
                millage=ad["millage"],
                fuel_type=ad["fuel_type"],
                transmission=ad["transmission"],
                horsepower=ad["horsepower"],
                color=ad["color"],
                moreInformation=ad["moreInformation"],
                main_image=image,
                # images_url = ad['images_url'] 
            )
            if ad:
                for image in ad["image_urls"]:
                    img = Image.objects.create(image=image, ad=ad)