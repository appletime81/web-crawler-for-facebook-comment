from init_driver import driver
from bs4 import BeautifulSoup
from pprint import pprint
import time


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
    time.sleep(1)

    # ------選取貼文顯示方式------
    post_present_method_btns = driver.find_elements_by_css_selector('span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7')
    for btn in post_present_method_btns:
        try:
            if btn.text in ['熱門貼文', '最新動態', '最新貼文', '最相關貼文']:
                btn.click()
                break
        except Exception:
            pass
    time.sleep(1)

    post_present_method_btns = driver.find_elements_by_css_selector('span.d2edcug0.hpfvmrgz.qv66sw1b')
    for btn in post_present_method_btns:
        try:
            if btn.text == '最新動態':
                btn.click()
                break
        except Exception:
            pass
    time.sleep(1)
    # -------------------------

    for i in range(3):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)


def get_posts(prefix_url):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    tags = soup.select('a')
    post_ids = list()
    for tag in tags:
        try:
            if 'posts' in tag.get('href'):
                post_ids.append(tag.get('href').split('/')[6])
        except:
            pass

    prefix_url = 'https://www.facebook.com/groups/999385510116409/posts/'
    post_ids = list(set(post_ids))
    post_urls = [prefix_url + post_id for post_id in post_ids]
    post_urls = sorted(post_urls, key=lambda x: int(x.split('/')[-1]), reverse=True)
    return post_urls


def get_recent_posts():
    pass


if __name__ == '__main__':
    browser_action()
    post_urls = get_posts(prefix_url=None)
    pprint(post_urls)
