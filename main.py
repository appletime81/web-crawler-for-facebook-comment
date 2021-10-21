import eel

# from get_latest_post import get_recent_posts


eel.init('web')


@eel.expose
def get_input_url(group_url):
    print(f'group url: {group_url}')


eel.start('index.html', size=(800, 800), port=5000)
