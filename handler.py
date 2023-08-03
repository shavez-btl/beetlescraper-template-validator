import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import requests
import json
import os

os.environ['BEETLE_SCRAPER_ENDPOINT'] = 'http://ec2-3-111-190-65.ap-south-1.compute.amazonaws.com:9090/api/beetlescraper/'
BEETLE_SCRAPER_ENDPOINT=os.getenv('BEETLE_SCRAPER_ENDPOINT')
print(BEETLE_SCRAPER_ENDPOINT)
def scraperValidation(event, context):
    driver, jsonObject=validateUrl()
    validateField(driver, jsonObject)
    driver.quit()

def validateUrl():
    resp=yamlDownload()
    json_object = json.loads(resp.text)
    print(json_object['ref_lp'])
    service = Service(executable_path='chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(json_object['ref_lp'])
        return driver, json_object
    except Exception as error:
        print("An exception occurred", error)

def validateField(driver, json_object):
    try:
        print(json_object['template_name'])
        for x in json_object['fields']:
            print(x['label'])
            if x['field_type']=="String":
                print(x['tag'])
                field = driver.find_elements(By.XPATH, x['tag'].replace('[]','1'))
                print(len(field))
                if len(field)==0:
                        # markAsReview()
                    print("mark as review")
                    break
    except Exception as error:
        print("An data exception occurred",error)

def markAsReview():
    url = BEETLE_SCRAPER_ENDPOINT+"scrapertemplate/markAsReview/2"
    response = requests.patch(url)
    print(response.text)

def yamlDownload():
    url = BEETLE_SCRAPER_ENDPOINT+"scrapertemplate/1/download"
    response = requests.get(url)
    # print(response.text)
    return response

def hello(event, context):
    scraperValidation({},{})
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# hello({},{})