#!/home/al/.venv/bin/python3

from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from xvfbwrapper import Xvfb
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from stem.control import Controller
from stem import Signal


def get_current_ip():
    display = Xvfb()
    display.start()
    ua = UserAgent()
    userAgent = ua.random
    options = Options()
    options.add_argument('user-agent={}'.format(userAgent))
    # PROXY = "socks5://localhost:9050"
    # options.add_argument('--proxy-server=%s' % PROXY)
    options.headless = True

    # driver = webdriver.Chrome(options=options, executable_path="/var/www/da-1.com/html/test/click-iframe/chromedriver")
    driver = webdriver.Chrome(options=options, executable_path="/var/www/html/test/click-iframe/chromedriver")
    # driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    # url = "http://da-1.com/test/click-iframe/a.html"
    url = "https://www.amkamdam.com/test/click-iframe/a.html"
    driver.get(url)
    try:
        driver.switch_to.frame('google_ads_iframe')
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="abgl"]'))).click()
    finally:
        driver.quit()
        display.stop()


def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="")
        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    for i in range(3):
        get_current_ip()
        # renew_tor_ip()
        # time.sleep(10)
