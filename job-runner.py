import json
from utils import createJobs, createUserScrapers, getAllScrapers, getAllTemplates, markAsDeleted, yamlDownload, scrapedDataDownload, getAllJobs, extractAllFields, markAsReview

def markScraperAsDeleted(event, context):
    scraperResp=getAllScrapers()
    scraperRespObject=json.loads(scraperResp.text)
    print(len(scraperRespObject['response']))
    for scraper  in scraperRespObject['response']:
        print(scraper['name'])
        markAsDeleted(scraper['id'])

def scraperJobRunner(event, context):
    markScraperAsDeleted({},{})
    templatesResp=getAllTemplates()
    templatesRespObject=json.loads(templatesResp.text)
    # print(templatesRespObject['response']['content'])
    print(len(templatesRespObject['response']['content']))
    userScraperList=[]
    for template in templatesRespObject['response']['content']:
        if template['status']=='ACTIVE':
            userScraperResp=createUserScrapers(template['id'],template['name'],template['templateUrl'])
            userScraperRespObject=json.loads(userScraperResp.text)
            userScraperList.append(userScraperRespObject['_embedded']['userScraperResponseModels'][0])
    print(len(userScraperList))
    print(userScraperList)
    for scrapers in userScraperList:
        createJobs(scrapers['id'],scrapers['scraperUrl'])
    
def jobRunner(event, context):
    scraperJobRunner({},{})
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

jobRunner({},{})