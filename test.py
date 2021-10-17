from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pprint import pprint
# 關閉通知
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument('disable-infobars')
options.add_argument('--window-size=1920,1080')

# open facebook
driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/groups/999385510116409/?ref=share')

# input email
time.sleep(2)  # 等待網頁跑完
account = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[1]/label/input')
account.send_keys('itrimsl8696@gmail.com')

password = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[2]/label/input')
password.send_keys('834159672~Nanonano')

driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[3]/div/div/div[1]/div/span/span').click()

time.sleep(15)
for i in range(20):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
# a = driver.find_elements_by_class_name("oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw")
# for i in range(len(a)):
#     print('------------------------------------------')
#     print(a[i].get_attribute('href'))

soup = BeautifulSoup(driver.page_source, "html.parser")
tags = soup.select('a')
post_ids = list()
for tag in tags:
    try:
        if 'posts' in tag.get('href'):
            print('-----------------------------------------------------------------------')
            print(tag.get('href'))
            post_ids.append(tag.get('href').split('/')[6])
    except:
        pass

post_ids = list(set(post_ids))
print('******************************************************')
pprint(post_ids)

# a =                          "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"
#     print(link.text)

