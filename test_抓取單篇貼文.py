from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pprint import pprint

options = webdriver.ChromeOptions()

# 關閉通知
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument('disable-infobars')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome('./chromedriver', options=options)


def browser_action():
    # open facebook
    driver.get('https://www.facebook.com/groups/1035885209777446/posts/5029962087036385/')

    # input email
    time.sleep(2)  # 等待網頁跑完
    account = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[1]/label/input')
    account.send_keys('itrimsl8696@gmail.com')

    # input password
    password = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[2]/label/input')
    password.send_keys('816357492~Nanonanonano')

    driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[3]/div/div/div[1]/div/span/span').click()

    # 把所有留言點擊出來
    time.sleep(5)
    all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d9wwppkn.fe6kdd0r.mau55g9w.c8b282yb.iv3no6db.jq4qci2q.a3bd9o3v.lrazzd5p.m9osqain")
    print(all_comment_btn)
    for i in all_comment_btn:
        print(i.text)


# def get_posts():
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     tags = soup.select('span')
#     post_ids = list()
#     for tag in tags:
#         try:
#             if 'posts' in tag.get('href'):
#                 # print('-----------------------------------------------------------------------')
#                 # print(tag.get('href'))
#                 post_ids.append(tag.get('href').split('/')[6])
#         except:
#             pass


if __name__ == '__main__':
    browser_action()