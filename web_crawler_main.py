import os

from init_driver import init_driver
from get_user_profile import browse_post, get_users
from get_group_url import get_group_url
from pprint import pprint
import time


def browser_action(driver, group_url, index):
    # open facebook
    driver.get(group_url)

    # 點擊登入按鈕
    try:
        driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/a[1]').click()
    except Exception:
        try:
            btns = driver.find_elements_by_xpath('//*[@id="mobile_login_bar"]/div[2]/div/a[1]')
            if btns:
                for btn in btns:
                    try:
                        btn.click()
                    except Exception:
                        pass
        except Exception:
            pass

    time.sleep(2)

    # 輸入帳密
    try:
        account_input = driver.find_element_by_xpath('//*[@id="m_login_email"]')
        account_input.send_keys('itrimsl8696@gmail.com')
        password_input = driver.find_element_by_xpath('//*[@id="m_login_password"]')
        password_input.send_keys('816357492~Nanonanonano')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="login_password_step_element"]/button').click()
    except Exception:
        pass

    # 捲動
    for i in range(3):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

    articles = driver.find_elements_by_tag_name('article')
    post_ids = []
    for article in articles:
        try:
            post_id = article.get_attribute('data-store')
            post_ids.append(post_id.split('.')[2].split(':')[0])
        except:
            print()
            pass

    post_ids = list(set(post_ids))
    post_ids = sorted(post_ids, key=lambda x: int(x), reverse=True)
    post_ids = post_ids[:5]
    print('--------------post ids-------------------------')
    pprint(post_ids)
    return post_ids


def generate_result(group_url, index):
    driver = init_driver()
    total_profile_list = []

    # 抓取post url，並排序
    group_url = group_url.replace("www.", "m.")
    post_ids = browser_action(driver, group_url, index)
    post_urls = [f'{group_url.replace("m.", "www.")}/posts/{post_id}' for post_id in post_ids]

    # 抓取用戶名稱，並儲存
    for i, post_url in enumerate(post_urls):
        browse_post(driver, post_url)
        user_profile_list = get_users(driver, post_ids[i], post_url, index)
        total_profile_list += user_profile_list
    return total_profile_list
