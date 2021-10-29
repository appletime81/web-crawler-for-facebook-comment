from bs4 import BeautifulSoup
import time
import re
from pprint import pprint

# global variables
comment_type_list = ['最相關留言', '最新', '所有留言']


def browse_post(driver, url):
    if 'groups' not in url:
        url = url.replace('www.', 'm.')

    driver.get(url)
    print(f'url: {url}')
    time.sleep(2)  # 等待網頁跑完

    # 把所有留言點擊出來
    all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b")
    for btn in all_comment_btn:
        try:
            if btn.text in comment_type_list:
                print('part1')
                btn.click()
                time.sleep(1)
                all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b")
                for btn in all_comment_btn:
                    try:
                        if btn.text == comment_type_list[2]:
                            btn.click()
                            time.sleep(3)
                            print('I am here')
                            ctrl = 1
                            while ctrl:
                                show_all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b")
                                ctrl = detect_more_comment(driver, show_all_comment_btn)
                    except Exception as e:
                        print(e)
            else:
                while True:
                    print('part2')
                    show_all_comment_btn = driver.find_elements_by_css_selector("span.d2edcug0.hpfvmrgz.qv66sw1b")
                    ctrl_num = detect_more_comment(driver, show_all_comment_btn)
                    if ctrl_num > 0:
                        pass
                    else:
                        print("It's break")
                        break
                break
        except Exception as e:
            print(e)


def detect_more_comment(driver, show_all_comment_btn):
    count = 0
    print('--------length-----------')
    print(len(show_all_comment_btn))
    for i, btn in enumerate(show_all_comment_btn):
        try:
            try:
                print('*************')
                print(i)
                print(btn.text)
            except:
                print('*************')
                print(i)
            if (
                '顯示先前' in btn.text or '檢視另' in btn.text or '查看其他' in btn.text or '則回覆' in btn.text
            ):
                if '隱藏' not in btn.text:
                    print('--------------------')
                    print(btn.text)
                    time.sleep(1)
                    try:
                        driver.execute_script("arguments[0].click();", btn)
                        print('已點擊')
                    except Exception as e:
                        print(e)

                    time.sleep(0.5)
                    count += 1
        except Exception as e:
            print(e)
    print(f'count: {count}')
    return count


# def get_users(driver, post_id, post_url, index):
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     tags = soup.select('a')
#     users = list()
#     for tag in tags:
#         try:
#             if 'group' in post_url:
#                 if '/user/' in tag.get('href'):
#                     users.append(tag.get('href'))
#             else:
#                 if 'fref=nf&rc=p&__tn__=R' in tag.get('href'):
#                     users.append(tag.get('href'))
#         except Exception:
#             pass
#     user_profile_list = list()
#     if 'group' in post_url:
#         for user in users:
#             if 'user' in user:
#                 user_text_list = user.split('/')
#                 user_id_index = user_text_list.index('user') + 1
#                 user_profile_list.append(f'https://www.facebook.com/profile.php?id={user_text_list[user_id_index]}\n')
#             # else:
#             #     id = re.search('id=\d+', user)[0]
#             #     user_profile_list.append(f'https://www.facebook.com/profile.php?{id}\n')
#     else:
#         for user in users:
#             user_profile_list.append(f'https://www.facebook.com{user}\n')
#
#     user_profile_list = list(set(user_profile_list))
#
#     print('-------------------------')
#     pprint(user_profile_list)
#
#     with open(f'{index}/{post_id}.txt', 'w') as f:
#         f.writelines(user_profile_list)

def get_users(driver, post_id, post_url, index):
    user_links = driver.find_elements_by_css_selector("a.oajrlxb2.g5ia77u1.qu0x051f")
    # get_attribute('href')
    user_profile_list = list()
    if 'group' in post_url:  # 抓取社團
        for user_link in user_links:
            try:
                link = user_link.get_attribute('href')
                if re.search('id=\d+', link):
                    id = re.search('id=\d+', link)[0]
                    user_profile_list.append(f'https://www.facebook.com/profile.php?{id}\n')
            except Exception:
                pass
    else:  # 抓取個人粉專
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tags = soup.select('a')
        users = list()
        for tag in tags:
            try:
                if 'fref=nf&rc=p&__tn__=R' in tag.get('href'):
                    users.append(tag.get('href'))
            except Exception:
                pass
        for user in users:
            user_profile_list.append(f'https://www.facebook.com{user}\n')

    user_profile_list = list(set(user_profile_list))
    with open(f'{index}/{post_id}.txt', 'w') as f:
        f.writelines(user_profile_list)