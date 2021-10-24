from bs4 import BeautifulSoup
from pprint import pprint


from bs4 import BeautifulSoup

soup = BeautifulSoup(open("(4) 權證小哥官方社團 _ Facebook.html"), "html.parser")
posts = soup.find_all('a')
post_url = []
for post in posts:
    try:
        if 'posts' in post.get('href'):
            post_url.append(post.get('href'))
    except:
        pass
pprint(post_url)
