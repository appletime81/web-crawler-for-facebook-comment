import eel
from web_crawler_main import *
import requests

eel.init('web')

with open('token.txt', 'r') as fp:
    lines = fp.readlines()
token = lines[0].replace('\n', '')


@eel.expose
def print_processing_status():
    return '執行中...'


@eel.expose
def print_ending_status():
    return '已完成!! 可進行下回操作'


@eel.expose
def main(group_urls):
    group_urls = filter_url(group_urls)
    notify_list = list()
    for i, group_url in enumerate(group_urls):
        try:
            os.mkdir(str(i + 1))
        except Exception:
            pass
        total_profile_list = generate_result(group_url, i + 1)
        total_profile_list = [f'社團{i + 1} {profile}' for profile in total_profile_list]
        notify_list.append(total_profile_list)

    for group_profile_list in notify_list:
        for profile in group_profile_list:
            line_notify(profile)


def filter_url(group_urls):  # 去掉為輸入的欄位傳進的空值
    group_urls = [url for url in group_urls if url != '']
    return group_urls


def line_notify(profile):
    headers = {
        "Authorization": "Bearer " + f"{token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": profile}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)


eel.start('index.html', size=(800, 800), port=8000, mode='edge')
