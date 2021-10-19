from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pprint import pprint


def browser_action():
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

    # open facebook
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get('https://www.facebook.com/groups/999385510116409/?ref=share')

    # input email
    time.sleep(2)  # 等待網頁跑完
    account = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[1]/label/input')
    account.send_keys('itrimsl8696@gmail.com')

    # input password
    password = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[2]/label/input')
    password.send_keys('834159672~Nanonano')

    driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[3]/div/div/div[1]/div/span/span').click()

    time.sleep(5)
    for i in range(80):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

    return driver


def get_posts(driver):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    tags = soup.select('a')
    post_ids = list()
    for tag in tags:
        try:
            if 'posts' in tag.get('href'):
                # print('-----------------------------------------------------------------------')
                # print(tag.get('href'))
                post_ids.append(tag.get('href').split('/')[6])
        except:
            pass

    post_ids = list(set(post_ids))
    print('******************************************************')
    print(len(post_ids))
    pprint(post_ids)


if __name__ == '__main__':
    driver = browser_action()
    get_posts(driver)

