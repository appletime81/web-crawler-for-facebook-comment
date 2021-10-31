import eel
from web_crawler_main import *

eel.init('web')


@eel.expose
def print_processing_status():
    return '執行中...'


@eel.expose
def print_ending_status():
    return '已完成!! 可進行下回操作'


@eel.expose
def main(group_urls):
    group_urls = filter_url(group_urls)
    for i, group_url in enumerate(group_urls):
        try:
            os.mkdir(str(i + 1))
        except Exception:
            pass
        generate_result(group_url, i + 1)


def filter_url(group_urls):  # 去掉為輸入的欄位傳進的空值
    group_urls = [url for url in group_urls if url != '']
    return group_urls


eel.start('index.html', size=(800, 800), port=8080)
