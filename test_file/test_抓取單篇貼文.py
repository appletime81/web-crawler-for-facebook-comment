from selenium import webdriver
from bs4 import BeautifulSoup
import time

start = time.time()
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

# global variables
comment_type_list = ['最相關留言', '最新', '所有留言']


def browser_action():
    # open facebook
    # driver.get('https://www.facebook.com/groups/999385510116409/posts/4039427482778848')
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
    all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b")
    for btn in all_comment_btn:
        try:
            if btn.text in comment_type_list:
                btn.click()
                time.sleep(1)
                all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b")
                for btn in all_comment_btn:
                    try:
                        if btn.text == comment_type_list[2]:
                            btn.click()
                            time.sleep(3)
                            ctrl = 1
                            while ctrl:
                                show_all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b")
                                ctrl = detect_see_more_comment(show_all_comment_btn)
                                # for i in range(10):
                                #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                                # time.sleep(3)
                    except Exception:
                        pass
        except Exception:
            pass


def detect_see_more_comment(show_all_comment_btn):
    count = 0
    for btn in show_all_comment_btn:
        try:
            if (
                '顯示先前' in btn.text or '檢視另' in btn.text or '查看其他' in btn.text or '則回覆' in btn.text
            ):
                print('--------------------')
                print(btn.text)
                time.sleep(1)
                try:
                    btn.click()
                    print('已點擊')
                except Exception as e:
                    try:
                        driver.execute_script("arguments[0].click();", btn)
                        print('已點擊')
                    except Exception as e:
                        print(e)

                time.sleep(0.5)
                count += 1
        except:
            pass
    return count


def get_users():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tags = soup.select('a')
    users = list()
    for tag in tags:
        try:
            if '/user/' in tag.get('href'):
                users.append(tag.get('href'))
        except Exception:
            pass

    user_profile_list = list()
    for user in users:
        user_text_list = user.split('/')
        user_id_index = user_text_list.index('user') + 1
        user_profile_list.append(f'https://www.facebook.com/profile.php?id={user_text_list[user_id_index]}\n')

    user_profile_list = list(set(user_profile_list))
    with open('user_profile.txt', 'w') as f:
        f.writelines(user_profile_list)


if __name__ == '__main__':
    browser_action()
    get_users()
    print(f'總執行時間: {time.time() - start}秒')
