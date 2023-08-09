import asyncio
import logging
import re
import math
import csv
from models import RaceResult
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from utilities import setup_logging

# setup logging configuration
setup_logging()


class BostonScraper:
    url = "http://registration.baa.org/cfm_Archive/iframe_ArchiveSearch.cfm?mode=entry&snap=59089571&"

    def __init__(self):
        self.pages = None
        self.results = []

    def determine_pages(self, html_content):
        # Find the total number of search results using a regular expression
        match = re.search(r'Your search\s+returned\s+(\d+)', html_content)

        # If the total number of search results was found, calculate the number of pages
        if match:
            total_results = int(match.group(1))
            logging.info(f'Total number of results found: {total_results}')
            pages = math.ceil(total_results / 25)
            logging.info(f'Number of Pages to scrape: {pages}')
        else:
            pages = 0

        self.pages = pages

    async def scrape_results(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch()

            browser_w_context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

            page = await browser_w_context.new_page()

            # Navigate to the page containing the form
            await page.goto(BostonScraper.url)

            # Select an option from the dropdowm
            await page.select_option('select[name="RaceYearLowID"]', '2019')

            # Select an option from the dropdowm
            await page.select_option('select[name="RaceYearHighID"]', '2019')

            # Submit the form
            await page.click('input[value="Search"]')

            # Wait for the page to load
            await page.wait_for_load_state("networkidle")

            # Get the HTML content of the page
            html_content = await page.content()

            # determine the number of pages
            self.determine_pages(html_content=html_content)

            # Iterate through the pages
            for i in range(self.pages):

                logging.info(f'Scraping Page {i} of {self.pages}')

                # Get the table element
                table = await page.query_selector('.tablegrid_table')

                # Get the HTML content of the table
                if table:
                    table_content = await table.inner_html()
                    self.parse_table(table_content)

                # Check if 'input[name="next"]' exists
                next_button = await page.query_selector('input[name="next"]')

                # If the next button exists, click it and wait for the page to load
                if next_button:
                    await next_button.click()
                    await page.wait_for_load_state("networkidle")

                # If the next button doesn't exist, break out of the loop
                else:
                    break

            # Close the browser
            await browser_w_context.close()

            # save results to csv
            self.save_data()

    def parse_table(self, table_html):
        soup = BeautifulSoup(table_html, 'lxml')

        # Find all main rows
        main_rows = soup.select('tr.tr_header')

        for main_row in main_rows:
            # Create a new Results instance
            result = RaceResult()

            # Parse the main row
            main_cols = main_row.select('td')

            result.year = int(main_cols[0].get_text(strip=True))
            result.bib = main_cols[1].get_text(strip=True)
            result.name = main_cols[2].get_text(strip=True)
            result.age = int(main_cols[3].get_text(strip=True))
            result.gender = main_cols[4].get_text(strip=True)
            result.city = main_cols[5].get_text(strip=True)
            result.state = main_cols[6].get_text(strip=True)
            result.country = main_cols[7].get_text(strip=True)

            # Parse the additional info row
            info_row = main_row.find_next_sibling('tr')
            info_cols = info_row.select('table.table_infogrid tr:nth-child(2) td')

            result.ranking_overall = info_cols[0].get_text().replace(" ", "")
            result.ranking_gender = info_cols[1].get_text().replace(" ", "")
            result.ranking_division = info_cols[2].get_text().replace(" ", "")
            result.official_time = info_cols[3].get_text(strip=True)
            result.net_time = info_cols[4].get_text(strip=True)

            # Append the Results instance to the results list
            self.results.append(result)
            logging.info(f'{len(self.results)} results scraped')

    def save_data(self):
        # Save the data to a CSV file
        with open('output/results.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=['year', 'bib', 'name', 'age', 'gender', 'city', 'state', 'country',
                                                   'ranking_overall', 'ranking_gender', 'ranking_division',
                                                   'official_time', 'net_time'])
            writer.writeheader()
            for result in self.results:
                writer.writerow(result.to_dict())


def main():
    scraper = BostonScraper()
    asyncio.run(scraper.scrape_results())


if __name__ == "__main__":
    main()
