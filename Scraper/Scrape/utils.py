import json
import logging
import os
from config_loader import config

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse

import logging

print(logging.getLogger().handlers)  # root handlers
print(logging.getLogger("scraper").handlers)
print(logging.getLogger("flask").handlers)

scraper_log=logging.getLogger("scraper")
scraper_log.setLevel(logging.INFO)

logging.basicConfig(
    filename="Logs/Scraper.log",
    level=logging.INFO,  # Change to DEBUG for more detail
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

PATH =config['paths']['scraping']['site_filters']

def load_website():
    if os.path.exists(PATH):
        with open(PATH, "r") as f:
            data=json.load(f)
        websites=data["websites"]
    return websites

def load_goodlist():
    if os.path.exists(PATH):
        with open(PATH, "r") as f:
            data=json.load(f)
        goodlist=data["goodlist"]
    return goodlist

websites = load_website()
goodlist = load_goodlist()

def setup_driver(): #Setup Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without GUI
    chrome_options.add_argument("--no-sandbox") # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) #Creates web driver instance


def is_browser_alive(driver):#Checks if a driver is healthy or not 
    try:
        driver.title  # Will raise error if session is invalid
        return True
    except:
        return False    
 

def write_to_json(cleaned_articles):  # Function to append articles to a JSON file
    file_path = config['paths']['scraping']['scraped_links']

    # Step 1: Load existing articles if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            try:
                existing_data = json.load(f)
                existing_articles = existing_data.get("articles", [])
            except json.JSONDecodeError:
                existing_articles = []
    else:
        existing_articles = []

    # Step 2: Append new articles, avoiding exact duplicates (optional)
    existing_articles.extend(cleaned_articles)

    # Step 3: Save back
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump({"articles": existing_articles}, f, indent=2, ensure_ascii=False)
