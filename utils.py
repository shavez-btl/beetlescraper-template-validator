from constants import BEETLE_SCRAPER_ENDPOINT
import requests
import json
from datetime import date,datetime

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

#create userScrapers from templates
def createJobs(scraperId,scraperUrl):
    url = BEETLE_SCRAPER_ENDPOINT+"jobConfig/createJobConfig"
    payload = json.dumps({
        "jobName": "Test Job",
        "userScraperId": scraperId,
        "jobType": "ADHOC",
        "targetUrl": scraperUrl
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response

#create userScrapers from templates
def createUserScrapers(id,name,templateUrl):
    url = BEETLE_SCRAPER_ENDPOINT+"scrapertemplate/useTemplate"
    payload = json.dumps({
        "templateId": id,
        "templateName": name + ' ' +str(datetime.now()),
        "templateGroupId": 1,
        "templateGroupName": "MHS",
        "scraperUrl": templateUrl
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response

#fetch all templates
def getAllTemplates():
    url = BEETLE_SCRAPER_ENDPOINT+"scrapertemplate/?size=25"
    response = requests.get(url)
    return response

#fetch all userScarpers
def getAllScrapers():
    url = BEETLE_SCRAPER_ENDPOINT+"userScraper/"
    response = requests.get(url)
    return response

#mark a scraper as DELETED
def markAsDeleted(scraperId):
    url = BEETLE_SCRAPER_ENDPOINT+"userScraper/patchUserScraper/"+str(scraperId)
    payload = json.dumps({
        "status": "DELETED"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.patch(url, headers=headers, data=payload)
    print(response.text)

#mark a template in review status
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