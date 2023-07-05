from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time


# URL 정보를 셋팅한다
URL_LOGIN = 'https://yeyak.guc.or.kr/member/login'

URL_REV_걸포 = 'https://yeyak.guc.or.kr/rent/reservation/index/2023/07/09/1/GIMPO05/03/2'
URL_REV_공설 = 'https://yeyak.guc.or.kr/rent/reservation/index/2023/07/09/1/GIMPO06/02/4'

# Chrome 드라이버 옵션 설정
options = Options()
options.add_argument('--start-maximized')  # 브라우저 최대화
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 감지 방지


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options= options))

# 웹사이트 열기
driver.get(URL_LOGIN)

id = 'youngjin333'
pwd = 'kyj159357'

# 로그인 진행
#driver.find_element(By.TAG_NAME('memid')).send_keys('youngjin333')
driver.find_element(By.ID,"input_memid").send_keys(id)
driver.find_element(By.ID,"input_mempw").send_keys(pwd)
driver.find_element(By.XPATH, "//input[@type='image'][@src='/images/member/btn_login.gif']").click()

time.sleep(1)

# 팝업창을 찾아본다
main = driver.window_handles
print(main)

for i in main:
    if i != main[0] :
        driver.switch_to.window(i)
        driver.close()

# main 창으로 switch진행
driver.switch_to.window(main[0])

# 특정 날짜로 변경
driver.get(URL_REV_걸포)

time.sleep(1)

# 시간을 선택한다.
#driver.find_element_by_id(task).click()
driver.find_element(By.ID, "select_4").click()

# 예약 신청 Click
driver.find_element(By.ID,"btn_reservation").click()

# 경고창 확인 버튼 클릭
Alert(driver).accept()

time.sleep(1)

# 기본 정보 입력

driver.find_element(By.NAME,'club_name').clear()
driver.find_element(By.NAME,'club_name').send_keys('김포스카이FC')
driver.find_element(By.NAME,'group_count').clear()
driver.find_element(By.NAME,'group_count').send_keys('1')
driver.find_element(By.NAME,'playname').clear()
driver.find_element(By.NAME,'playname').send_keys('축구경기')
driver.find_element(By.ID,'agree_1').click()
# # 브라우저 종료
# driver.quit()

time.sleep(100)

# driver.implicitly_wait(100)

