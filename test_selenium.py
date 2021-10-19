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
    driver.get('https://www.facebook.com/groups/999385510116409/?ref=share')

    # input email
    time.sleep(2)  # 等待網頁跑完
    account = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[1]/label/input')
    account.send_keys('itrimsl8696@gmail.com')

    # input password
    password = driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[2]/label/input')
    password.send_keys('816357492~Nanonanonano')

    driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/div[3]/div/div/div[1]/div/span/span').click()

    time.sleep(5)
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)


def get_posts():
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

    prefix_url = 'https://www.facebook.com/groups/999385510116409/posts/'
    post_ids = list(set(post_ids))
    post_urls = [prefix_url + post_id for post_id in post_ids]
    post_urls = sorted(post_urls, key=lambda x: int(x.split('/')[-1]), reverse=True)
    print('******************************************************')
    print(len(post_ids))
    pprint(post_urls)
    return post_urls


def get_users(post_url):
    pass



if __name__ == '__main__':
    browser_action()
    post_urls = get_posts()
    get_users(post_urls[0])
    # a =  'https://www.facebook.com/groups/999385510116409/posts/4116814041706858'
    # print(a.split('/')[-1])

