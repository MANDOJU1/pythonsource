# 파이썬 검색 뉴스기사 크롤링
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def main(keyword):

    url = "https://news.google.com/search?q=" + keyword + "=ko&gl=KR&ceid=KR%3Ako"

    try:

        with requests.Session() as s:
            r = s.get(url)
            soup = BeautifulSoup(r.text, "lxml")
            # print(soup)

            news_clipping = data_extract(soup)

            for news in news_clipping:
                for k, v in news.items():
                    print(f"{k} : {v}")

    except HTTPError as e:
        print(e.code)


def data_extract(soup):
    # article 영역 찾기
    # #yDmH0d > c-wiz > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(1) > c-wiz > article

    articles = soup.select("div.UW0SDc article")
    base_url = "http://news/google.com"

    # [{"title": "", "href": "", "writer": "", "report_date": "report_time"}] 이 방식으로 담고 싶음
    news = []
    news_items = {}

    for article in articles:
        # print(article)

        # 제목을 가지고 있는 요소 찾기
        link_title = article.select_one("div > div:nth-child(2) a")
        # print(link_tilte)

        # 제목 추출
        news_items["title"] = link_title.text

        # 뉴스 기사 링크 추출
        # href = link_title["href"]  # ./articles/CBMiMGh0dHA6Ly93d3cuYm9hbm5ld3MuY29tL21lZGlhL3ZpZXcuYXNwP2lkeD05NTg4M9IBAA?hl=ko&gl=KR&ceid=KR%3Ako
        news_items["href"] = base_url + link_title["href"][1:]

        # 작성자
        news_items["writer"] = article.select_one("div.a7P8l > div").text

        # 작성일자와 시간 2024-05-20T00:58:00Z
        # T 기준으로 분리
        report_date_time = article.select_one("time")
        # <time class="hvbAAd" datetime="2024-05-20T00:58:00Z">8일 전</time>

        # 기사 일자와 시간이 없는 경우 오류 방지
        if report_date_time:
            # split 은 [] 리스트로 돌려줌 ['2024-05-20', '00:58:00Z']
            report_date_time = report_date_time["datetime"].split("T")
            news_items["report_date"] = report_date_time[0]
            news_items["report_time"] = report_date_time[1]
        else:
            news_items["report_date"] = ""
            news_items["report_time"] = ""

        # print(title, href, writer, report_date, report_time)

        news.append(news_items)
        news_items = {}

    print(news[:3])
    return news


if __name__ == "__main__":
    main("아이폰")
