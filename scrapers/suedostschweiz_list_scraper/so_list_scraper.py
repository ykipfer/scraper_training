# Import necessary modules
from models import Ad, BaseProtocol, BaseScraper
from utilities import setup_logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import math

# Set up logging
setup_logging()


# Define Protocol class
class ProtocolSuedostschweiz(BaseProtocol):
    def __init__(self, main_url):
        # Initialize variables
        super().__init__(main_url)
        self.count_all_pages = 0
        self.count_all_ads = 0
        self.count_ads_per_page = 20


class ScraperSuedostschweiz(BaseScraper):
    def __init__(self, protocol):
        super().__init__(protocol)

    def update_counts_in_protocol(self) -> None:
        """Counts all ads (regardless of date) and number of pages."""
        # Send request to the website and parse the response
        url = "https://www.suedostschweizjobs.ch/jobs?page=0"
        source = requests.get(url, headers=self.headers).text
        soup = BeautifulSoup(source, 'lxml')
        # Update total number of ads and pages in the protocol
        count_all_ads_str = soup.find('h1', class_='search-result-header').text
        self.protocol.count_all_ads = int(''.join(d for d in count_all_ads_str if d.isdigit()))
        self.protocol.count_all_pages = math.ceil(self.protocol.count_all_ads / self.protocol.count_ads_per_page)

    def scrape_ads(self):
        # Update counts in the protocol
        self.update_counts_in_protocol()
        # Loop through each page and scrape the ads
        for current_page_num in range(self.protocol.count_all_pages):
            url = self.protocol.main_url + str(current_page_num)
            source = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(source.content, 'lxml')
            # Find the ads
            ads_divs = soup.find_all('article')
            # Loop through each ad and extract the information
            for ad_div in ads_divs:
                ad = Ad()
                ad.id = ad_div['id'].replace('node-', '')
                ad.url = 'https://www.suedostschweizjobs.ch' + ad_div['about']
                ad.title = ad_div.find('h2').text
                try:
                    ad.company = ad_div.find('span', class_='recruiter-company-profile-job-organization').a.text
                except AttributeError:
                    ad.company = None
                try:
                    ad.location = ad_div.find('div', class_='location').span.text
                except AttributeError:
                    ad.location = None
                ad.date_published = datetime.strptime(ad_div.find('span', class_='date').text.replace(',', '').strip(),
                                                      '%d.%m.%Y').date()
                # Add the ad to the protocol
                self.protocol.add_ad(ad)

        # Filter out ads that are older than 7 days
        self.protocol.filter_ads()


def main():
    # Main function to scrape the ads and save the data
    scraper = ScraperSuedostschweiz(ProtocolSuedostschweiz(main_url="https://www.suedostschweizjobs.ch/jobs?page="))
    scraper.scrape_ads()
    scraper.save_data()


# Run the main function if the script is run as a standalone program
if __name__ == "__main__":
    main()
