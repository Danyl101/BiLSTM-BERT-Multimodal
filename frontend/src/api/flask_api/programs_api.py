from flask_cors import CORS
from flask import Flask
import json
from flask import Blueprint,request, jsonify
from Scraper.Extract.Extract_run import extract_run
from Scraper.Scrape.Scrape_run import run_scrape
from Scraper.Scrape.utils import scraper_log
from Scraper.Extract.utils import extract_log

scraper_log.propagate = False
extract_log.propagate = False

app=Flask(__name__)
CORS(app)

from .utils import logging

bp = Blueprint("programs_api", __name__) #Defines blueprint for the api 

@bp.route("/api/run-scrape", methods=["POST"]) #Web Link Endpoint
def scrape():
    try:
        scraper_log
        data=run_scrape() #Runs python file from backend
        return jsonify({"status":"success"})
    except Exception as e:
        logging.error(f"Failed to run scraping {e}")

@bp.route("/api/run-extract",methods=["POST"]) #Web Link Endpoint
def extract():
    try:
        extract_log
        data=extract_run() #Runs python file from backend
        return jsonify({"status":"success"})
    except Exception as e:
        logging.error(f"Failed to run extraction {e}")  
        
if __name__ == "__main__":
    app.run(debug=True, port=5000)