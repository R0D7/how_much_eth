from requests import Request, Session
import json

def get_eth_price_():
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {
        "slug":"ethereum",
        "convert" : "USD"
    }
    headers = {
        "Acceps":"application/json",
        # Insert your API key instead of "API_KEY"
        "X-CMC_PRO_API_KEY":"API_KEY"
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)

    # Get the price of ethereum from the response of coinmarketcap
    return float(json.loads(response.text)['data']["1027"]["quote"]["USD"]['price'])