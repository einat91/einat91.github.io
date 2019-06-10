import pandas
import requests
from bs4 import BeautifulSoup
page = requests.get("https://weather.com/en-IN/weather/today/l/5c95b44a2f64030b0186c9671a0ddda2a0a4934130e0935e5c484ddf93d6a9bc")
content = page.content
soup = BeautifulSoup(content, "html.parser")

city = soup.find("div", {"class": "twc-header-mobile__location-content"}).find("span").text
temp = soup.find("span", {"class": "styles__temperature"}).find("span").text
cond = soup.find("span", {"class": "styles__narrative"}).find("div").text
feels = soup.find("span", {"class": "styles__value"}).find("span").text
wind = soup.find("span", {"class": "styles__value"}).find("span").text
humidity = soup.find("span", {"class": "styles__value"}).find("span").text

print(city)
print(temp)
print(cond)
print(feels)
print(wind)
print(humidity)

city.to_csv("output.txt")
temp.to_csv("output.txt")
cond.to_csv("output.txt")
feels.to_csv("output.txt")
wind.to_csv("output.txt")
humidity.to_csv("output.txt")
