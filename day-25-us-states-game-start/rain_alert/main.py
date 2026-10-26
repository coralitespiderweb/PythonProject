import requests
import smtplib
import os

my_email = "wenxin.zhou@warriorlife.net"
password = "gydmzbjbrfhnzpav"
api_key = os.environ.get("OWM_API_KEY")
print(api_key)

parameters = {
    "lat": 37.338207,
    "lon": -121.886330,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

print(weather_data['cod'])
print(weather_data)
print(weather_data['list'][0]["weather"][0]["id"])

#condition_codes = [code for list_item in weather_data['list'][(0, 3)]["weather"][0]["id"]]
condition_codes = [list_item["weather"][0]["id"] for list_item in weather_data['list']]
print(condition_codes)

will_rain = False

for condition_code in condition_codes:
    if condition_code < 800:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Bring an umbrella.\n\n"
        )
