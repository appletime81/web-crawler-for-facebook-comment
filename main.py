import eel

# from get_latest_post import get_recent_posts


eel.init('web')


@eel.expose
def main(group_url):
    group_url = filter_url(group_url)
    print_url(group_url)


def print_url(group_url):
    print(group_url)


def filter_url(group_url):  # 去掉為輸入的欄位傳進的空值
    group_url = [url for url in group_url if url != '']
    return group_url


eel.start('index.html', size=(800, 800), port=5000)
