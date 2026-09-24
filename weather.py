
import requests
print("let build simple weather application")
location = input("location")
date= input("date(YYYY-MM-DD)")
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}"
response = requests.get(url, params={'key': "HCU2HJXB7N2U8K26NM4E4W5GE"})
data = response.json()
print(f"the weather of {location} on the date{date} is :{data['description']}")