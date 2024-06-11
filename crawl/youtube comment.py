from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import pandas as pd


def main():
    browser = set_chrome_driver()

    url = "https://www.youtube.com/watch?v=HosW0gulISQ"
    browser.get(url)

    time.sleep(2)

    # 스크롤 움직이기
    # 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
    interval = 5

    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.documentElement.scrollHeight")

    while True:
        browser.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight)"
        )

        time.sleep(interval)

        cur_height = browser.execute_script(
            "return document.documentElement.scrollHeight"
        )

        if cur_height == prev_height:
            break

        prev_height = cur_height

    # 스크롤 처음으로 움직이기
    browser.execute_script("window.scrollTo(0,0)")

    time.sleep(3)

    # 전체 소스를 BeautifulSoup 담기
    soup = BeautifulSoup(browser.page_source, "lxml")

    # 댓글 사용자의 아이디 및 코멘트 가져오기
    # selector 복사 : #author-text > span
    ids = soup.select("#author-text > span")
    # selector 복사 : #content-text > span
    commnets = soup.select("#content-text > span")

    ids_list = []
    commnets_list = []
    # 확인
    for idx in range(len(ids)):
        # print(ids[idx].text.strip(), commnets[idx].text.strip())

        clean_id = ids[idx].text.strip()
        clean_id = clean_id.replace("\n", " ")
        clean_id = clean_id.replace("\t", " ")
        ids_list.append(clean_id)

        clean_comment = commnets[idx].text.strip()
        clean_comment = clean_comment.replace("\n", " ")
        clean_comment = clean_comment.replace("\t", " ")
        commnets_list.append(clean_comment)

    # 데이터프레임 생성
    dict_data = {"Id": ids_list, "Comments": commnets_list}
    df = pd.DataFrame(dict_data)

    df.to_csv("./crawl/file/youtube.csv", index=False)

    time.sleep(5)


def set_chrome_driver():
    options = ChromeOptions()
    # options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


if __name__ == "__main__":
    main()
