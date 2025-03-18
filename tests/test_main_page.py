# tests/test_main_page.py

import time
import pytest
import urllib.parse as parse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# 예외를 사용하려면 임포트 필요
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# src 폴더에 정의된 MainPage 클래스를 가져옴
from src.main_page import MainPage  

# 이 클래스의 모든 테스트가 conftest.py의 driver 픽스처를 사용함
@pytest.mark.usefixtures("driver")
class TestMainPage:
    def test_search_items(self, driver: WebDriver):
        """
        검색창에 상품명을 입력하고 검색하면 상품 결과가 로드되는지 확인하는 테스트"
        """
        # 1. MainPage 객체 생성 및 페이지 열기
        main_page = MainPage(driver)
        main_page.open()
        # 2. "노트북"이라는 검색어를 입력하여 검색 수행
        main_page.search_items("노트북")

        # 3. WebDriverWait을 사용하여 검색 결과가 나타날 때까지 대기
        wait = WebDriverWait(driver, 10)
        # 예시: 쿠팡의 검색 결과는 li.search-product 요소들로 구성 (실제 CSS 셀렉터는 상황에 따라 변경)
        items = driver.find_elements(By.CSS_SELECTOR, "li.search-product")
        # 4. 검색 결과가 하나 이상 있는지 검증
        assert len(items) > 0

        time.sleep(5)


@pytest.mark.skip(reason = "테스트 케이스 발동 안함")
class TestMainPage:
    def test_open_main_page(self, driver: WebDriver):
        """
        쿠팡 메인 페이지가 올바르게 열리는지 확인하는 테스트
        """
        # 1. MainPage 객체 생성
        main_page = MainPage(driver)
        # 2. 페이지 열기
        main_page.open()
        time.sleep(2)

        # 3. URL에 "coupang.com"이 포함되어 있는지 확인
        wait = WebDriverWait(driver, 10)  # 최대 10초까지 기다림
        wait.until(EC.url_contains("coupang.com"))
        assert "coupang.com" in driver.current_url

        # 예시: 로그인 버튼 클릭 (만약 해당 기능이 구현되어 있다면)
        # main_page.click_login("로그인")  # 구현된 메서드에 맞게 호출