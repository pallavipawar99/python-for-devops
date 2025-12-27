
import requests
import json

def get_api_data(symbol):
    apikey = "demo"
    baseUrl = "https://www.alphavantage.co/"
    query = f"query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={apikey}"

    response = requests.get(url=baseUrl+query)
    data = response.json()
    res = write_data_to_file(data)
    if res == True:
        print("data written to file successfully")
    else : 
         print("data not written to file")

def write_data_to_file(data):
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)
    return True 
     
# FOR e.g user_input = IBM
user_input = input("Enter symbol of which data u want")
get_api_data(user_input)

