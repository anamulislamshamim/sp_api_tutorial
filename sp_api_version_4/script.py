import requests 
import urllib.parse 
import datetime
import json 
from credentials import credentials

# Getting the LWA access token using the Seller central 
# App credentials. The token will be valid for 1 hour

token_response = requests.post(
    url="https://api.amazon.com/auth/o2/token",
    data={
        "grant_type": "refresh_token",
        "refresh_token": credentials["refresh_token"],
        "client_id": credentials["lwa_app_id"],
        "client_secret": credentials["lwa_client_secret"],
    },
)


accesss_token = token_response.json()["access_token"]

# endpoint for North America (Canada, US, Mexico, and Brazil marketplaces)
end_point = "https://sellingpartnerapi-na.amazon.com" 

# Canadian market place id 
market_place_id = "A2EUQ1WTGCTBG2" 

# requests params for make a request to order endpoint 
request_params = {
    "MarketplaceIds": market_place_id, # required parameter
    "CreatedAfter": (
        datetime.datetime.now() - datetime.timedelta(days=30)
    ).isoformat(), # orders created since 30 days ago, the date needs to be the ISO format
}


# make the request 
orders = requests.get(
    url=end_point + 
    "/orders/v0/orders" + 
    "?" + 
    urllib.parse.urlencode(request_params),
    headers={
        'x-amz-access-token': accesss_token,
    }
)


# pretty print the JSON response 
print(json.dumps(orders.json(), indent=2))