import time
from selenium import webdriver
import platform


with open('comment.txt') as comment:
    comments = comment.read()




def auto_comment(striped_comment, url):
    time.sleep(2)

    browser.get(url)
    count = 0
    for sc in striped_comment:

        cb = browser.find_element_by_css_selector("textarea[name='comment_text']")
        cb.send_keys(sc)

        button = browser.find_element_by_css_selector("input[type='submit']")
        button.click()

        time.sleep(2)
        print(f'{sc} comment is done !!')
        count = count + 1
        if count == 1:
            break

def urlrun():
    time.sleep(2)
    for url in urls:
        auto_comment(striped_comment, url)
if __name__ == "__main__":
    while True:
        striped_comment = comments.replace(' ', "")
        striped_comment = striped_comment.split('\n')
        emails = ['wwr3b5ef.xef@kjjit.eu','w0ve0xcx.bpc@kjjit.eu']
        your_password = 'Thisismynewaccount123'
        for your_email in emails:
            if platform.system()=='Darwin':
                browser = webdriver.Chrome('chromedrivers/chromedrivermac')
            elif platform.system()=='Windows':
                browser = webdriver.Chrome('chromedrivers/chromedriverwin.exe')
            elif platform.system()=='Linux':
                browser = webdriver.Chrome('chromedrivers/chromedriverlinux')

            browser.get("https://mbasic.facebook.com")
            email = browser.find_element_by_css_selector("input[name='email']")
            email.send_keys(str(your_email))
            time.sleep(1)

            password = browser.find_element_by_css_selector("input[name='pass']")
            password.send_keys(str(your_password))
            button = browser.find_element_by_css_selector("input[type='submit']")
            button.click()
            urls = ['https://mbasic.facebook.com/103688321034034/photos/a.103688377700695/106230464113153/']
            urlrun()
            browser.close()
