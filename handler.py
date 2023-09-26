import json
from utils import createJobs, createUserScrapers, getAllTemplates, yamlDownload, scrapedDataDownload, getAllJobs, extractAllFields, markAsReview

def scraperValidation(event, context):
    # templatesResp=getAllTemplates()
    # templatesRespObject=json.loads(templatesResp.text)
    # # print(templatesRespObject['response']['content'])
    # print(len(templatesRespObject['response']['content']))
    # userScraperList=[]
    # for template in templatesRespObject['response']['content']:
    #     if template['status']=='ACTIVE':
    #         userScraperResp=createUserScrapers(template['id'],template['name'],template['templateUrl'])
    #         userScraperRespObject=json.loads(userScraperResp.text)
    #         userScraperList.append(userScraperRespObject['_embedded']['userScraperResponseModels'][0])
    # print(len(userScraperList))
    # print(userScraperList)
    # for scrapers in userScraperList:
    #     createJobs(scrapers['id'],scrapers['scraperUrl'])
    resp=getAllJobs()
    json_object = json.loads(resp.text)
    print(json_object)
    scrapedDataJson={}
    print(len(json_object['response']['content']))
    for job in json_object['response']['content']:
        print(job['jobConfigJobName'])
        yamlData=yamlDownload(job['userScraperId'])
        yamlDataJson=json.loads(yamlData.text)
        extractedFields=extractAllFields(yamlDataJson['fields']) #extracting all they keys of userScraper yaml data
        print(extractedFields)
        scrapedData=scrapedDataDownload(job['userScraperId'], job['id'])
        if len(scrapedData.text)>0:
            scrapedDataJson=json.loads(scrapedData.text)
            print(list(scrapedDataJson['data'].keys()))
            compareResult=compareKeys(list(scrapedDataJson['data'].keys()),extractedFields) #checking if keys are same for userScraper yaml data & scraped data for a job
            if compareResult:
                if checkNullValues(scrapedDataJson['data']): #checking if scraped data has null values
                    print("Valid")
                else:
                    print("Invalid...Mark As Review")
            else:
                print("Invalid!!!  Mark As Review")
        else:
            print("No Data!!!")

def compareKeys(scrapedKeys, yamlKeys):
    scrapedKeys.sort()
    yamlKeys.sort()
    if(scrapedKeys==yamlKeys):
      return True
    else:
      return False

def checkNullValues(scrapedData):
    for obj in scrapedData.keys():
        print(obj, scrapedData[obj],sep=" -> ")
        if scrapedData[obj]=="":
            return False
    return True

def validator(event, context):
    scraperValidation({},{})
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

validator({},{})