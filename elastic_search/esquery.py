import boto3
import requests
from requests_aws4auth import AWS4Auth

def get_awsauth(elastic_search_endpoint):
    host = elastic_search_endpoint
    session = boto3.session.Session()
    region = session.region_name
    service = 'es'
    credentials = boto3.Session().get_credentials()
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
    return awsauth



def query(elastic_search_endpoint, query, field, awsauth):
    r = requests.get('https://{}/product/product/_search?q={}:{}&size=100'.format(elastic_search_endpoint, field, query)
                     ,auth=awsauth)
    rjson = r.json()
    return rjson


