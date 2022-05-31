import os
import csv
import bs4
import requests
from logs import logger
from config import Config
from scraping_manager.automate import Web_scraping

jobs_ids = []

def main (): 

    # Read categories, keywords and locations from json
    credentials = Config()
    keywords = credentials.get("keywords")
    locations = credentials.get("locations")

    # Create and open csv / database file
    csv_path = os.path.join (os.path.dirname(__file__), f"data.csv")
    csv_file = open(csv_path, "a", encoding="utf-8", newline="")
    csv_writter = csv.writer(csv_file)

    # Write colum titles 
    headers = ["keyword", "location", "title", "company", "date"]
    csv_writter.writerow (headers)

    # Open chrome
    scraper = Web_scraping()

    # Search each keyword
    for keyword in keywords:

        # Search location
        for location in locations:

            # Loop fopr extract all pages
            current_page = 1
            selector_next_page = 'span[title="Siguiente"]'
            while True:

                # Print status
                logger.info (f"Scraping data of {keyword} in {location}, page: {current_page}")

                # generate url with keyword and location
                location_formated = location.lower().replace(' ', '%20')
                keyword_formated = keyword.lower().replace(' ', '%20')

                url = f"https://www.linkedin.com/jobs/search/?keywords={keyword_formated}&location={location_formated}"

                # Load page
                scraper.set_page (url)

                # Debug lines
                # with open (os.path.join (os.path.dirname (__file__), "temp.html"), "w", encoding="UTF-8") as file:
                #     file.write (res.text)
                # break
                
                # Generate css selectors for get data
                selector_article = "ul.jobs-search__results-list li"

                # Get number of articles in the current page
                articles = scraper.get_elems (selector_article)
                
                # Get data from each article
                for article_num in range(1, len(articles)+1):

                    selector_current_article = f"{selector_article}:nth-child({article_num}) div"
                    selector_title = f"{selector_current_article} .base-search-card__info h3"
                    selector_company = f"{selector_current_article} .base-search-card__info h4"
                    selector_date = f"{selector_current_article} time"

                    # Skeip duplicated jobs
                    id = scraper.get_attrib (selector_current_article, "data-tracking-id")
                    if id in jobs_ids:
                        continue
                    else:
                        jobs_ids.append (id)

                    # Get job data
                    title = scraper.get_text (selector_title)
                    company = scraper.get_text (selector_company)
                    date = scraper.get_text (selector_date)
                    
                    # Clean data
                    title = title.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    company = company.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    date = date.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")

                    # Add data to csv
                    row_data = [keyword, location, title, company, date]
                    csv_writter.writerow (row_data)
                    print (row_data)

                # Go down for load more results
                break

            # Debug lines
            break

        # Debug lines
        break

    # Close and save data in csv file
    csv_file.close ()


if __name__ == "__main__":

    main()