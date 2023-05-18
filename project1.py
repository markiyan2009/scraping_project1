import requests as r
from bs4 import BeautifulSoup
import lxml
import json
headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
url = "https://prom.ua/ua/Elektroskutera-elektromototsikly"
req = r.get(url, headers=headers)
src = req.text
with open("project1Folder/index.html","w", encoding="utf-8") as file:
  file.write(src)
with open("project1Folder/index.html" , encoding="utf-8") as file:
   src = file.read()
soup = BeautifulSoup(src,"lxml")
name_bikes= soup.find_all("span",class_="_3Trjq _7NHpZ QrtcH U32Rk")
prise= soup.find_all("div",class_="bkjEo")
all = dict()
for i in range(len(name_bikes)):
    if name_bikes[i] != name_bikes[-1]:
        all[name_bikes[i].text] = prise[i].text

with open("project1Folder/items.json","w") as file:
   json.dump(all,file,indent=4,ensure_ascii=False)
with open("project1Folder/items.json") as file:
   all = json.load(file)

for item in all:
    print(item)
    print(all[item])
    print("---")
           
