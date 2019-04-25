# 다음 실시간 검색 순위 크롤링
import requests
from bs4 import BeautifulSoup

url = 'https://www.daum.net/'
req = requests.get(url)

if req.status_code == requests.codes.ok:
    print("접속 성공")
    html = BeautifulSoup(req.text, 'html.parser')
    items = html.select('.realtime_part .roll_txt')

    for item in items:
        link = item.select_one('.link_issue')
        keyword = item.select_one('.link_issue')
        rank = item.select_one('.ir_wa')

        print(rank.text, keyword.text, link['href'])
else:
    print("접속 실패")
