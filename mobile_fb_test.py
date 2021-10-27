from init_driver import driver
from bs4 import BeautifulSoup
from get_user_profile import browse_post, get_users
from pprint import pprint
import time

GROUP_URL = 'https://m.facebook.com/groups/999385510116409'


def browser_action():
    # open facebook
    driver.get(GROUP_URL)

    # 點擊登入按鈕
    driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/a[1]').click()
    time.sleep(2)

    # 輸入帳密
    account_input = driver.find_element_by_xpath('//*[@id="m_login_email"]')
    account_input.send_keys('itrimsl8696@gmail.com')
    password_input = driver.find_element_by_xpath('//*[@id="m_login_password"]')
    password_input.send_keys('816357492~Nanonanonano')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login_password_step_element"]/button').click()

    # 捲動
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

    articles = driver.find_elements_by_tag_name('article')
    post_ids = []
    for article in articles:
        try:
            post_id = article.get_attribute('data-store')
            post_ids.append(post_id.split('.')[2].split(':')[0])
        except:
            pass

    post_ids = list(set(post_ids))
    post_ids = sorted(post_ids, key=lambda x: int(x), reverse=True)
    pprint(post_ids)
    return post_ids


def generate_post_url():
    post_ids = browser_action()
    post_urls = [f'https://www.facebook.com/groups/999385510116409/{post_id}' for post_id in post_ids]
    for i, post_url in enumerate(post_urls):
        browse_post(driver, post_url)
        get_users(driver, post_ids[i])


if __name__ == '__main__':
    generate_post_url()
