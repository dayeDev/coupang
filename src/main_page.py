# src/main_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

class MainPage:
    # 쿠팡 메인 페이지 URL과 검색창의 HTML id 값
    url = "https://www.coupang.com"
    SEARCH_INPUT_ID = "headerSearchKeyword"  # 실제 HTML에서 확인한 id 값

    def __init__(self, driver: WebDriver):
        # Selenium WebDriver 인스턴스를 받아서 저장
        self.driver = driver

    def open(self):
        """
        쿠팡 메인 페이지를 연다.
        """
        self.driver.get(self.url)

    def search_items(self, item_name: str):
        """
        검색창에 상품명을 입력하고, Enter 키를 눌러 검색을 수행한다.
        """
        search_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        search_box.clear()                   # 검색창 초기화
        search_box.send_keys(item_name)      # 검색어 입력
        search_box.send_keys(Keys.ENTER)      # Enter 키로 검색 실행
