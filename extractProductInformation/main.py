import requests 
from sp_api.api import Products, Catalog, Sales
from sp_api.base import SellingApiException, Marketplaces, SellingApiForbiddenException, Granularity
from sp_api.api import Orders, CatalogItems
from datetime import datetime, timedelta, date 
import json 
from typing import List 
from pprint import pprint 


secrets = 'keys.json'
with open(secrets) as f:
    KEYS = json.loads(f.read())
    

def get_secret(setting) -> List(any):
    try:
        return KEYS[setting] 
    except KeyError:
        msg = "Set the {} environment variable".format(setting)
        raise KeyError(msg)


LWA_APP_ID = get_secret('lwa_app_id')
LWA_CLIENT_SECRET = get_secret('lwa_client_secret')
AWS_SECRET_KEY = get_secret('aws_secret_key')
AWS_ACCESS_KEY = get_secret('aws_access_key')
ROLE_ARN = get_secret('role_arn')
CLIENTS_REFRESH_TOKEN = get_secret('clients_refresh_token') 


client_config = dict(
    refresh_token = CLIENTS_REFRESH_TOKEN,
    lwa_app_id = LWA_APP_ID,
    lwa_client_secret = LWA_CLIENT_SECRET,
    aws_secret_keys = AWS_SECRET_KEY,
    aws_access_key = AWS_ACCESS_KEY,
    role_arn = ROLE_ARN,
)


# extract information for a particular product 
band_asin = 'B088DZWSF6'
res = Products(credentials=client_config, marketplace=Marketplaces.US)
data = res.get_item_offers(asin=band_asin, item_condition='New')
pprint(data.payload)