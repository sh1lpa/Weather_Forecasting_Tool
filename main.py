import requests
import json

def get_config():

    with open('D:\Project\Weather_Forecasting_Tool\config.json') as f:
        data = json.load(f)
        return data

def main():

    req = ''
    while req !='q':
        req = input('Please enter the City name  (or q to exit) :')
                # config['city name'] = text
        param = {"q":req,"appid": "api_key","units": "metric"}
        # print(param)
        try:

            r = requests.get("https://api.openweathermap.org/data/2.5/weather",params=param)

            

            if r.status_code == 200:
                response = r.json()
                
                print("Weather : %s\nTemperature : %5.2f \nDescription : %s" % (response["weather"][0]["main"], response["main"]["temp"],response["weather"][0]["description"]))
            else:
                print("Invalid City")
        except requests.exceptions.HTTPError as errh:
            print("Invalid City (Enter a valid city : )")


if __name__ == '__main__':
    main()