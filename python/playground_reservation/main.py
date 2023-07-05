from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


# Chrome 드라이버 옵션 설정
options = Options()
options.add_argument('--start-maximized')  # 브라우저 최대화
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 감지 방지


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options= options))

# 웹사이트 열기
driver.get('https://yeyak.guc.or.kr/')
# driver.get('https://google.com')

# # 웹 요소 찾기 및 조작 예제
# element = driver.find_element(By.ID, 'myElement')  # ID가 'myElement'인 요소 찾기
# element.click()  # 요소 클릭
# element.send_keys('Hello, World!')  # 텍스트 입력
# element.send_keys(Keys.ENTER)  # 엔터 키 입력

# # 브라우저 종료
# driver.quit()

time.sleep(100)

# driver.implicitly_wait(100)
