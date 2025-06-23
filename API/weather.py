import requests
import json
import datetime

key="f7c01d229e31a1aa6be01972f97a5e2d"
lat=float(input("latitude: "))
lon=float(input("longitude: "))
part=""

url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={part}&appid={key}&units=metric"

response=requests.get(url)

print("status code:",response.status_code)

if response.status_code==200:
    data=response.json()
    # print(json.dumps(data, indent=2))

    sunrise_timestamp=data["sys"]["sunrise"]

    sunrise=datetime.datetime.fromtimestamp(sunrise_timestamp)

    sunset_timestamp=data["sys"]["sunset"]

    sunset=datetime.datetime.fromtimestamp(sunset_timestamp)

    place="Thapathali"

    sky=data["weather"][0]["description"]


    temperature=data["main"]["temp"]
    print(f"""WEATHER REPORT OF {place}:sunrise:{sunrise}
sunset:{sunset}
temperatue:{temperature}
sky:{sky} """)
     
else:
    print("error: ",response.status_code)
   



 

