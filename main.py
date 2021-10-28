import eel
from mobile_fb_test import *

eel.init('web')

status = 'Ready to Start'


@eel.expose
def print_processing_status():
    global status
    return status


@eel.expose
def main(group_urls):
    global status
    group_urls = filter_url(group_urls)
    status = 'Processing....'
    for i, group_url in enumerate(group_urls):
        generate_post_url(group_url, i + 1)
    status = 'Done'


def filter_url(group_urls):  # 去掉為輸入的欄位傳進的空值
    group_urls = [url for url in group_urls if url != '']
    return group_urls


eel.start('index.html', size=(800, 800), port=8080)
