# LinkedIn Scraper

Create a scraper that will go to [LinkedIn](https://www.linkedin.com/jobs/search?keywords=&location=&geoId=&trk=guest_homepage-basic_jobs-search-bar_search-submit&position=1&pageNum=0) and scrape the following information for ads from Switzerlabd:
- ad ID
- ad title
- ad location
- date published
- url to ad content
- ad company

Only scrape ads that are no older than 7 days.

## Setup
Use the following modules to create the scraper:
- [requests](https://requests.readthedocs.io/en/latest/)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

To install these modules run:
```bash
pip install requests
pip install beautifulsoup4
```