## 🖥️ 쿠팡 웹페이지 자동화
셀레니움을 통해 웹페이지 자동화를 하고 파이테스트를 통해 기능 정의 및 코드 테스트 진행<br>
Automate webpages with Selenium and define features and test code with Pytest

## 🛠️ 기술 스택
- Selenium
- python
- Pytest

## 📁 프로젝트 구조
```
coupang/
│── src/         
│   ├── __init__.py          # 패키지 인식 파일
│   └── main_page.py         # 실제 기능 구현 파일
└── page/           
│   ├── __init__.py
│   ├── conftest.py          # 공통 픽스처 정의 파일
│   └──  test_main_page.py   # main_page.py에 대한 테스트 코드 파일
└──  report.html             # 결과 리포트 파일
```
