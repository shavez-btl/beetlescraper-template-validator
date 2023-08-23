from constants import BEETLE_SCRAPER_ENDPOINT
import requests
import json
from datetime import date

#extract all keys in fields in userScraper Yaml Data
def extractAllFields(yamlData):
    ef=[]
    for field in yamlData:
        ef.append(field['label'])
    return ef

#fetch all jobs for todays date and admin user
def getAllJobs():
    url = BEETLE_SCRAPER_ENDPOINT+"job/filter/search"
    payload = json.dumps({
        "searchTerm": "",
        "userScraperIds": [],
        "status": None,
        "userId": [1],
        "jobStartDate": {
          "fromDate": date.today().strftime("%d/%m/%Y"),
          "toDate": date.today().strftime("%d/%m/%Y"),
        },
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response

#mark a teamplate in review status
def markAsReview():
    url = BEETLE_SCRAPER_ENDPOINT+"scrapertemplate/markAsReview/2"
    response = requests.patch(url)
    print(response.text)

#download userScraper Yaml Data
def yamlDownload(id):
    url = BEETLE_SCRAPER_ENDPOINT+"/userScraper/"+str(id)+"/download"
    response = requests.get(url)
    return response

#download scraped data of a job
def scrapedDataDownload(userScraperId,jobId):
    url = BEETLE_SCRAPER_ENDPOINT+"job/scrapedData"
    payload = json.dumps({
        "userScraperId": userScraperId,
        "jobId": jobId
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response