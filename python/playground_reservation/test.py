from selenium import webdriver
from datetime import date
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# # Print description
# def print_description():
#     desc = [
# 	    '1:  06:00 ~ 07:00',
# 		'2:  07:00 ~ 08:00',
# 		'3:  08:00 ~ 09:00',
# 		'4:  09:00 ~ 10:00',
# 		'5:  10:00 ~ 11:00',
# 		'6:  11:00 ~ 12:00',
# 		'7:  12:00 ~ 13:00',
# 		'8:  13:00 ~ 14:00',
# 		'9:  14:00 ~ 15:00',
# 		'10: 15:00 ~ 16:00',
# 		'11: 16:00 ~ 17:00',
# 		'12: 17:00 ~ 18:00',
# 		'13: 18:00 ~ 19:00',
# 		'14: 19:00 ~ 20:00',
# 		'15: 20:00 ~ 21:00',
# 		'16: 21:00 ~ 22:00',
# 		'ex) Time : 4 5 6'
# 	]
#     print('\n'.join(desc))
#     print()

# print_description()

# # INPUT
# # U_ID = input('ID : ')
# # U_PW = input('PW : ')
# T_MONTH = input('Month : ')
# T_DAY = input('Day : ')
# T_TIME = list(map(int, input('Time : ').split()))

# Login Info
LOGIN_INFO = {
    'user_id': 'watcom1',
	'user_pw': '7105moon',
	'fc_name': '장기스카이',
	'fc_count': '30',
	'play_name': '축구경기'
}

# URL : 김포시설공단


URL_LOGIN = 'https://yeyak.guc.or.kr/member/login'

# URL : 걸포축구장 예약
# URL_RESERVE = "https://yeyak.guc.or.kr/rent/reservation/index/2021/{}/{}/1/GIMPO05/03/2".format(T_MONTH,T_DAY)

# URL : 공설축구장 예약
#URL_RESERVE = "http://yeyak.gp.or.kr/rent/reservation/index/2020/{}/{}/1/GIMPO06/02".format(T_MONTH,T_DAY)

# Chrome start
# driver = webdriver.Chrome('./chromedriver.exe')
options = Options()
options.add_argument('--start-maximized')  # 브라우저 최대화
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 감지 방지


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options= options))


# Chrome 드라이버 인스턴스 생성
# driver = webdriver.Chrome(service=webdriver_service, options=options)

#
# try:
	# 1. 예약시간 parsing
	# T_TIME_SEL = list()
	# for t in T_TIME:
	# 	T_TIME_SEL.append('select_'+str(t))
	
	# 2. Login
	driver.get('https://yeyak.guc.or.kr/member/login')
	#driver.implicitly_wait(3)
	
	# driver.find_element_by_name('memid').send_keys(LOGIN_INFO['user_id'])
	# driver.find_element_by_name('mempw').send_keys(LOGIN_INFO['user_pw'])
	# driver.find_element_by_xpath("//input[@type='image'][@src='/images/member/btn_login.gif']").click()
	
	# # 3. 예약일자 선택
	# print(URL_RESERVE)
	# driver.get(URL_RESERVE)
	# driver.implicitly_wait(3)
	
	# # 4. 예약시간 선택
	# for task in T_TIME_SEL:
	# 	print(task)
	# 	driver.find_element_by_id(task).click()
	# 	'''
	# 	if(isChecked()):
	# 	'''
		
	# # 5. 예약신청 (일시 확정)
	# driver.find_element_by_id('btn_reservation').click()
	
	# # 6. 예약신청 (FC 정보 입력 : 단체명/단체인원수/행사명)
	# driver.find_element_by_name('club_name').clear()
	# driver.find_element_by_name('club_name').send_keys(LOGIN_INFO['fc_name'])
	# driver.find_element_by_name('group_count').clear()
	# driver.find_element_by_name('group_count').send_keys(LOGIN_INFO['fc_count'])
	# driver.find_element_by_name('playname').clear()
	# driver.find_element_by_name('playname').send_keys(LOGIN_INFO['play_name'])
	# driver.find_element_by_id('agree_1').click()
	# driver.find_element_by_id('btn_reservation').click()
	
	# # 7. 완료 (screenshot)
	# today = date.today()
	# driver.get_screenshot_as_file('screenshot-'+today.isoformat()+'.png')
	
# except Exception as e:
# 	print('Exception = {}'.format(e))

# finally:
# 	driver.implicitly_wait(3)
# 	driver.quit()

	

