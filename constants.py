import os

os.environ['BEETLE_SCRAPER_ENDPOINT'] = 'http://ec2-3-111-190-65.ap-south-1.compute.amazonaws.com:9090/api/beetlescraper/'
BEETLE_SCRAPER_ENDPOINT=os.getenv('BEETLE_SCRAPER_ENDPOINT')