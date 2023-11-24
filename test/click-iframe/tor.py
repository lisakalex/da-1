#!/home/al/.venv/bin/python3
# from telnetlib import EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from xvfbwrapper import Xvfb  # stopped working
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from stem.control import Controller
from stem import Signal


def get_current_ip():
    # display = Xvfb()
    # display.start()
    ua = UserAgent()
    userAgent = ua.random
    options = Options()
    options.add_argument('user-agent={}'.format(userAgent))
    PROXY = "socks5://localhost:9050"
    options.add_argument('--proxy-server=%s' % PROXY)
    options.headless = True
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    # executable_path has been deprecated, please pass in a Service object

    driver = webdriver.Chrome(options=options, executable_path="/var/www/da-1.com/html/test/click-iframe/chromedriver")
    # driver = webdriver.Chrome(options=options, executable_path="/var/www/html/test/click-iframe/chromedriver")
    # driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    # url = "http://da-1.com/test/click-iframe/a.html"
    url = "https://www.amkamdam.com/test/click-iframe/a.html"
    driver.get(url)
    try:
        # driver.switch_to.frame('buttonframe')
        # driver.find_element(By.ID, 'abgl').click()
        # element = driver.find_element(By.CLASS_NAME, 'huy')
        # driver.execute_script("""
        # var element = arguments[0];
        # element.remove();
        # """, element)

        driver.switch_to.frame('google_ads_iframe')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="abgl"]'))).click()

        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div[1]/div[2]/div[2]/button[1]'))).click()
        # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "google_ads_iframe_/27823234/GFG_Desktop_LeftSideBar_Docked_160x600_0")))
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "abgl"))).click()

        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div[1]/div[2]/div[2]/button[1]'))).click()
        # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "google_ads_iframe_/27823234/GFG_Desktop_LeftSideBar_Docked_160x600_0")))
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "abgl"))).click()
        #
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/button[1]'))).click()

        # driver.switch_to.frame('buttonframe')
        # driver.find_element(By.CLASS_NAME, 'fc-button fc-cta-consent fc-primary-button').click()
        # element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'fc-button fc-cta-consent fc-primary-button'))).click()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div[1]/div[2]/div[2]/button[1]'))).click()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Consent'))).click()
        # driver.switch_to.frame('buttonframe')
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "abgl"))).click()
        # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "google_ads_iframe_/27823234/GFG_Desktop_LeftSideBar_Docked_160x600_0"))).click()
        # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "google_ads_iframe_/27823234/GFG_Desktop_RightSideBar_ATF_300x250_2_0"))).click()
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "abgl"))).click()
        # driver.switch_to.frame('google_ads_iframe_/27823234/GFG_Desktop_LeftSideBar_Docked_160x600_0')
        # driver.find_element(By.ID, 'abgl').click()

        # driver.set_script_timeout(30)

        # driver.implicitly_wait(10)
        # delay = 3  # seconds
        # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'abgl')))

        # driver.findElement(By.cssSelector("a[href='/docs/configuration']")).click();
        # driver.find_element("value of link text")
        # iframe = driver.find_element(By.CSS_SELECTOR, "#google_ads_iframe_/27823234/GFG_Desktop_LeftSideBar_Docked_160x600_0__container__ > iframe")
        # driver.switch_to.frame(iframe)
        # driver.implicitly_wait(10)
        # driver.switch_to.frame('google_ads_iframe_/27823234/GFG_Desktop_LeftSideBar_Docked_160x600_0')
        # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "google_ads_iframe_/27823234/GFG_Desktop_LeftSideBar_Docked_160x600_0")))
        # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "buttonframe")))
        # driver.switch_to.frame('buttonframe')
        # element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "abgl")))

        # iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
        # driver.switch_to.frame(iframe)
        # element.click()
        # driver.find_element(By.TAG_NAME, 'a').click()
        # driver.switch_to.default_content()

        # This Wont work
        # driver.find_element(By.TAG_NAME, 'a').click()

        # iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
        # driver.switch_to.frame('buttonframe')
        # driver.switch_to.frame(iframe)
        # driver.find_element(By.ID, 'abgl').click()
        # driver.switch_to.default_content()

    finally:
        driver.quit()
    # display.stop()


def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="")
        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    for i in range(5):
        get_current_ip()
        renew_tor_ip()
        time.sleep(10)
