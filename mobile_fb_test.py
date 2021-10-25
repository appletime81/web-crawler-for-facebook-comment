from init_driver import driver
from bs4 import BeautifulSoup
from pprint import pprint
import time
import pyautogui


def browser_action():
    # open facebook
    driver.get('https://m.facebook.com/groups/999385510116409?sorting_setting=CHRONOLOGICAL')

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
    driver.get(f'https://www.facebook.com/groups/999385510116409/posts/{post_ids[0]}')


def url_processing(data):
    pass


if __name__ == '__main__':
    browser_action()
    # post_urls = get_posts(prefix_url=None)
    # pprint(post_urls)
    a = {
        "linkdata": 'qid.-7536756313661453306:mf_story_key.4324613607593566:top_level_post_id.4324613607593566:tl_objid.4324613607593566:content_owner_id_new.100003727074732:page_id.999385510116409:src.22:story_location.6:filter.GroupStoriesByActivityEntQuery:ott.AX8dnfnt0yZLkap1:tds_flgs.3:page_insights.{\"999385510116409\":{\"page_id\":999385510116409,\"page_id_type\":\"group\",\"actor_id\":100003727074732,\"dm\":{\"isShare\":0,\"originalPostOwnerID\":0},\"psn\":\"EntGroupMallPostCreationStory\",\"post_context\":{\"object_fbtype\":657,\"publish_time\":1633163994,\"story_name\":\"EntGroupMallPostCreationStory\",\"story_fbid\":[4324613607593566]},\"role\":1,\"sl\":6}}',
        "feedback_target": 4324613607593566,
        "feedback_source": 2,
        "action_source": 0,
        "actor_id": 100003824025972}
