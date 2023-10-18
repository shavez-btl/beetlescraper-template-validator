import json
from utils import createJobs, createUserScrapers, getAllScrapers, getAllTemplates, markAsDeleted, run
def markScraperAsDeleted(event, context,token):
    scraperResp=getAllScrapers(token)
    scraperRespObject=json.loads(scraperResp.text)
    print(len(scraperRespObject['response']))
    for scraper  in scraperRespObject['response']:
        print(scraper['name'])
        markAsDeleted(scraper['id'],token)

def scraperJobRunner(event, context,token):
    markScraperAsDeleted({},{},token)
    templatesResp=getAllTemplates(token)
    templatesRespObject=json.loads(templatesResp.text)
    # print(templatesRespObject['response']['content'])
    print(len(templatesRespObject['response']['content']))
    userScraperList=[]
    for template in templatesRespObject['response']['content']:
        if template['status']=='ACTIVE':
            userScraperResp=createUserScrapers(template['id'],template['name'],template['templateUrl'],token)
            userScraperRespObject=json.loads(userScraperResp.text)
            userScraperList.append(userScraperRespObject['_embedded']['userScraperResponseModels'][0])
    print(len(userScraperList))
    print(userScraperList)
    for scrapers in userScraperList:
        createJobs(scrapers['id'],scrapers['scraperUrl'],token)
    
def jobRunner(event, context):
    token=run({},{})
    print(token)
    scraperJobRunner({},{},token)
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

jobRunner({},{})