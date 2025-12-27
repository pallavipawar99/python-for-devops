
import requests
import json

def get_api_data(symbol):
    try:
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
    except:
        print("Error occured while running script")

def write_data_to_file(data):
    try:
        with open("output.json", "w") as f:
            json.dump(data, f, indent=4)
        return True 
    except:
        print("Error Occured while writting data to file")
        return False
     

user_input = input("Enter symbol of which data u want")
get_api_data(user_input)
# FOR e.g user_input = IBM
