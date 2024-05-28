import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook

# openpyxl workbook 생성
wb = Workbook()  # 새 워크북 생성
ws = wb.active  # 현재 활성화된 sheet 가져옴

ws.title = "네이버open"
# 너비 조정
ws.column_dimensions["B"].width = 100
ws.column_dimensions["C"].width = 60

ws.append(["순위", "상품명", "판매주소"])


headers = {
    "X-Naver-Client-Id": "ULYpF6gqPQquxLzGSKnd",
    "X-Naver-Client-Secret": "Uf9zLplNzo",
}


start, num = 1, 1
for idx in range(10):
    # idx : 0 ~ 9
    start_num = start + (idx * 100)
    url = "https://openapi.naver.com/v1/search/shop.json"
    params = {"query": "아이폰", "display": "100", "start": str(start_num)}
    r = requests.get(url, headers=headers, params=params)

    # print(r.url)

# json 가져오기
data = r.json()
# print(data)
# print(data["items"])
for idx, item in enumerate(data["items"], 1):
    # print(idx, item["title"], item["link"])  # <b>아이폰</b>
    ws.append([num, item["title"], item["link"]])
    num += 1


base_dir = "./crawl/file/"
wb.save(base_dir + "naver.xlsx")
wb.close()
