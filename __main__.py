import os
import csv
import time
from logs import logger
from config import Config
from scraping_manager.automate import Web_scraping

jobs_ids = []

def main (): 

    # Read categories, keywords and locations from json
    credentials = Config()
    keywords = credentials.get("keywords")
    locations = credentials.get("locations")
    show_chrome = credentials.get("show_chrome")

    # Create and open csv / database file
    csv_path = os.path.join (os.path.dirname(__file__), f"data.csv")
    csv_file = open(csv_path, "a", encoding="utf-8", newline="")
    csv_writter = csv.writer(csv_file)

    # Write colum titles 
    headers = ["keyword", "location", "title", "company", "date"]
    csv_writter.writerow (headers)

    # Open chrome
    scraper = Web_scraping(headless=not show_chrome)

    # Search each keyword
    for keyword in keywords:

        # Search location
        for location in locations:

            # Print status
            logger.info (f"Scraping data of {keyword} in {location}")

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

            # Load all jobs
            articles_num = 0
            while True:
                last_articles_num = len(scraper.get_elems (selector_article))
                scraper.go_bottom ()
                time.sleep (3)
                new_articles_num = len(scraper.get_elems (selector_article))
                if last_articles_num == new_articles_num:
                    articles_num = new_articles_num
                    break
            
            # Get data from each article
            for article_num in range(1, articles_num+1):

                selector_current_article = f"{selector_article}:nth-child({article_num}) div"
                selector_title = f"{selector_current_article} h3"
                selector_company = f"{selector_current_article} h4"
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

            # Debug lines
            # break

        # Debug lines
        # break

    # Close and save data in csv file
    csv_file.close ()


if __name__ == "__main__":

    main()