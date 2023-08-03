from datetime import datetime, timedelta
import csv

class Ad:

    def __init__(self):
        self.id = None
        self.url = None
        self.title = None
        self.company = None
        self.location = None
        self.date_published = None

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "date_published": self.date_published
        }

class BaseProtocol:

    def __init__(self, main_url):
        self.main_url = main_url
        self.ads = []

    def add_ad(self, ad):
        # Method to add an ad to the list
        self.ads.append(ad)

    def get_ads(self):
        # Method to retrieve the list of ads
        return self.ads

    def filter_ads(self):
        # Filter out ads that are older than 7 days
        self.ads = [ad for ad in self.ads if ad.date_published > (datetime.now() - timedelta(days=7)).date()]

class BaseScraper:

    def __init__(self, protocol):
        self.protocol = protocol
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def scrape_ads(self):
        raise NotImplementedError("Please implement this method")

    def save_data(self):
        # Save the data to a CSV file
        ads_list = self.protocol.get_ads()
        with open('output/ads.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'url', 'title', 'company', 'location', 'date_published'])
            writer.writeheader()
            for ad in ads_list:
                writer.writerow(ad.to_dict())