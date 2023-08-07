# Boston Marathon Scraper

Create a Scraper goes to the following link: http://registration.baa.org/cfm_Archive/iframe_ArchiveSearch.cfm and scrapes
all results from 2019.

Since we are dealing with form data, we need to use [playwright](https://playwright.dev) or [selenium](https://www.selenium.dev) to scrape the results. I recommend using playwright, since the setup is much easier.
To start use `sync_playwright` to create a synchronous scraper.


## Setup

First we need to install the playwright module.

```bash
pip install playwright
```

After installing playwright via pip you need to run the following command to install the browsers extensions.

```bash
playwright install
```

You might also need to install the following modules:

```bash
pip install csv # needed to save results to CSV
pip install math # contains useful math functions
pip install re # allows you to use regular expressions
pip install asyncio # module for asynchronous programming
```
## Additional Tasks
Once you've created a synchronous scraper using `sync_playwright`, try using `async_playwright` and `asyncio` to run an asynchronous scraper. Go to the following links for more documentation on [asyncio](https://realpython.com/async-io-python/) and [asynch_playwright](https://playwright.dev/python/docs/library)