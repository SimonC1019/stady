import requests
from bs4 import BeautifulSoup

url="http://www.lez.com.tw/report/CHIU_index_1.html"
html=requests.get(url)
html.encoding="Big5"
sp = BeautifulSoup(html.text, "html.parser")

data =sp.find_all("input")

data1 =(sp.select('input')[0].get('name'))
print(data)
print(data1)