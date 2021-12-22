import requests
from bs4 import BeautifulSoup

url="https://www.taiwanlottery.com.tw/"
html=requests.get(url)
#html.encoding="utf-8"
sp = BeautifulSoup(html.text, 'html.parser')

datas = sp.find('div',class_='contents_box06')
print(datas)

title = datas.find('span' , 'font_black15').text
print(title)

nums= datas.find_all('div',class_='ball_tx ball_blue')
"""
xx=[]
for i in range(0,12):
    xx.append(nums[i].text)
xx.sort()
print(xx)
"""
nums.text.sort()
print(nums)