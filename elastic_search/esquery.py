import requests


def query(query, field, elastic_search_endpoint, master_user, master_user_password):
    r = requests.get('https://{}/product/product/_search?q={}:{}&size=100'.format(elastic_search_endpoint, field, query)
                     ,auth=(master_user, master_user_password))
    rjson = r.json()
    return rjson


