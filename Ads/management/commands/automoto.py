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
        print(f"Fetching data from URL: {url}")

        ad_info = scrape_single_ad(url)
        