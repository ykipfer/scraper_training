# Südostschweizjobs.ch Scraper

Create a scraper that will go to [Südostschweizjobs.ch](https://www.suedostschweizjobs.ch) and scrape the following information from the ads:
- ad ID
- ad title
- ad location
- date published
- url to ad content
- ad company

Only scrape ads that are no older than 7 days and save the results under `output/ads.csv`.

## Setup
Use the following modules to create the scraper:
- [requests](https://requests.readthedocs.io/en/latest/)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

To install these modules run:
```bash
pip install requests
pip install beautifulsoup4
```