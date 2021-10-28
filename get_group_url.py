def get_group_url(group_urls):
    group_urls = [group_url.replace('www', 'm') for group_url in group_urls]
    return group_urls
