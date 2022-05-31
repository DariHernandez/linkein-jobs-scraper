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
                selector_article = "#p_ofertas article"
                selector_title = f"{selector_article} h1"
                selector_company = f"{selector_article} .fs16.fc_base.mt5.mb10"
                selector_details = f"{selector_article} .fc_aux.t_word_wrap.mb10.hide_m"
                selector_date = f"{selector_article} .fs13.fc_aux"

                # Get number of articles in the current page
                soup = bs4.BeautifulSoup (res.text, "html.parser")
                articles = soup.select (selector_article)
                
                # Get data from each article
                for article in articles:

                    # Skeip duplicated jobs
                    id = article.get ("id")
                    if id in jobs_ids:
                        continue
                    else:
                        jobs_ids.append (id)

                    # Get job data
                    title = article.select (selector_title)[0].getText()
                    company = article.select (selector_company)[0].getText()
                    details = article.select (selector_details)[0].getText()
                    date = article.select (selector_date)[0].getText().strip()
                    
                    # Clean data
                    title = title.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    company = company.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    details = details.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")
                    date = date.strip().replace("\n", "").replace (",", "").replace ("\r\r", " ").replace ("\r", "")

                    # Add data to csv
                    row_data = [keyword, location, title, company, details, date]
                    csv_writter.writerow (row_data)

                next_button = soup.select (selector_next_page)
                if next_button:
                    current_page+=1
                else:
                    break

            # Debug lines
            break

        # Debug lines
        break

    # Close and save data in csv file
    csv_file.close ()


if __name__ == "__main__":

    main()