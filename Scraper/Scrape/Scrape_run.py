from .link_extract import scrape_multiple_sites
from .utils import logging,websites,goodlist

def run_scrape():
    print(websites)
    print(goodlist)
    cleaned_articles = scrape_multiple_sites(websites, max_scrolls=15)
    logging.info(f"Total articles scraped: {len(cleaned_articles)}") #Returns no of articles that are available after cleaning
    
if __name__ == "__main__":
    run_scrape()
    
   