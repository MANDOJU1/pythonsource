from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from urllib.request import urlretrieve


def main():
    browser = set_chrome_driver()

    browser.get("https://www.naver.com")

    # 검색 창 찾기

    # 페이지에서 요소 찾기 : find_element(기준, 기준에 맞는 이름), find_elements()
    element = browser.find_element(By.ID, "query")

    # 검색어 입력 + 엔터
    element.send_keys("아이스크림")
    element.send_keys(Keys.ENTER)

    time.sleep(2)

    # div.api_flicking_wrap > div > a → selector 요소로 찾기
    browser.find_element(
        By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a'
    ).click()

    time.sleep(5)

    # 스크롤 움직이기
    # 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
    interval = 3
    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        time.sleep(interval)

        cur_height = browser.execute_script("return document.body.scrollHeight")

        if cur_height == prev_height:
            break

        prev_height = cur_height

    # 스크롤 처음으로 움직이기
    browser.execute_script("window.scrollTo(0,0)")
    # 작은 이미지를 찾아오기
    time.sleep(3)

    images = browser.find_elements(By.CSS_SELECTOR, ".thumb img")

    count = 1
    for img in images:
        try:
            img.click()
            time.sleep(2)

            time.sleep(5)

            # 큰이미지 //*[@id="main_pack"]/section[1]/div/div/div[1]/div[2]/div[1]/img
            # div.viewer_image img
            img_url = browser.find_element(
                By.CSS_SELECTOR, "div.viewer_image img"
            ).get_attribute("src")
            print(img_url)

            # urlretrieve("다운로드 받을 파일 경로", "저장경로")
            urlretrieve(img_url, "./crawl/download/" + str(count) + ".jpg")
            count += 1
        except:
            pass


def set_chrome_driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


if __name__ == "__main__":
    main()
