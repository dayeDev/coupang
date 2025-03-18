# tests/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# driver 픽스처: 각 테스트 함수마다 새로운 WebDriver 인스턴스를 생성하고, 테스트 종료 후 quit() 함.
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # 브라우저가 자동화된 것처럼 보이지 않게 하기 위한 설정
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0")
    # SSL 인증서 에러 무시
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    # 자동화 관련 설정 제거
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # Sandbox, DevShm 관련 문제 우회 (리눅스/맥 등에서 적용 가능)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ChromeDriver 객체 생성 (Service()는 ChromeDriver 경로를 자동으로 처리)
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    # 암묵적 대기: 요소 찾을 때 최대 5초까지 기다림
    driver.implicitly_wait(5)
    
    # 테스트 실행 전에 driver 객체를 yield로 전달
    yield driver
    
    # 테스트가 끝나면 브라우저 종료
    driver.quit()
