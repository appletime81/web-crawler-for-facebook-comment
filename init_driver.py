from selenium import webdriver


def init_driver():
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
    return driver


driver = init_driver()
