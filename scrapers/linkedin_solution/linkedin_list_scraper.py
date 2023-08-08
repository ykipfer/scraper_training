import requests
import re
from models import Ad, BaseProtocol, BaseScraper
from utilities import setup_logging
from bs4 import BeautifulSoup
from datetime import datetime

# Set up logging
setup_logging()


class ProtocolLinkedin(BaseProtocol):
    def __init__(self, main_url):
        super().__init__(main_url)
        self.page_range = range(0, 1000, 25)
        self.urls = [f'{self.main_url}{page}' for page in self.page_range]


class ScraperLinkedin(BaseScraper):
    def __init__(self, protocol):
        super().__init__(protocol)

    def scrape_ads(self):
        """ Extracts raw HTML containing ads from LinkedIn """
        for url in self.protocol.urls:
            source = requests.get(url=url, headers=self.headers)
            soup = BeautifulSoup(source.content, 'lxml')
            ads_raw = soup.find_all('div', class_='job-search-card')

            for ad_raw in ads_raw:

                # List of different date variations
                date_classes = ['job-result-card__listdate', 'job-search-card__listdate--new',
                                'job-search-card__listdate']

                date_string = None
                for date_class in date_classes:
                    date_container = ad_raw.find('time', class_=date_class)
                    if date_container is not None:
                        date_string = date_container['datetime']
                        break  # Exit the loop as soon as we find a date

                ad = Ad()
                ad.url = ad_raw.find('a', class_='base-card__full-link')['href'].split('?')[0]
                ad.id = re.search(r"\d+$", ad.url).group()
                ad.title = ad_raw.find('h3', class_='base-search-card__title').get_text().strip()
                ad.company = ad_raw.find('h4').get_text().strip()
                ad.location = ad_raw.find('span', class_='job-search-card__location').get_text().strip()
                ad.date_published = datetime.strptime(date_string, "%Y-%m-%d").date() if date_string is not None else None

                self.protocol.add_ad(ad)

        self.protocol.filter_ads()


def main():
    # Main function to scrape the ads and save the data
    scraper = ScraperLinkedin(ProtocolLinkedin(main_url="https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=Schweiz&locationId=&geoId=106693272&f_TPR=r604800&start="))
    scraper.scrape_ads()
    scraper.save_data()


if __name__ == "__main__":
    main()
