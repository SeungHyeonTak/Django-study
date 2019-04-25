# 웹 페이지에 접근해서 데이터를 가져온다
# requests는 ajax로 받아온 데이터를 실시간으로 반영 가능
# 받아온 데이터는 소스보기에서 보는 소스까지만 있음

# selenium : 웹 브라우저를 원격 조작하는 방식의 크롤러
# selenium, scrapy

import requests

# 가져온 데이터를 HTML로 해석함
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

req = requests.get(url)

if req.status_code == requests.code.ok:
    print("접속 성공")
    html  = BeautifulSoup(req.text, "html.parser")
    items = html.select(".PM_CL_realtimeKeyword_list_base .ah_item")

    for item in items:
        link = item.select_one('.ah_a')
        keyword = item.select_one('.ah_k')
        rank = item.select_one('.ah_r')

        print(rank.text, keyword.text, link['href'])
else:
    print("접속 실패")
