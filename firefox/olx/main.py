import threading
import time

from selenium import webdriver
import logging
import login as l
import search as s

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def pop_up(driver):
    pop = 0
    while pop == 0:
        try:
            pop_button = driver.find_element_by_css_selector('.m0zy07y')
            pop = 1
        except:
            time.sleep(10)
            print("no element")
            pop = 0
            pop_button.click()

    print('pop are denide')


if __name__ == "__main__":
    url = 'https://www.olx.pl/'
    driver = webdriver.Firefox(executable_path='/home/ruxuge/Dokumenty/geckodriver')
    driver.get(url)
    driver.maximize_window()
    element = driver.find_element_by_id('onetrust-accept-btn-handler')
    element.click()
    #b = threading.Thread(target=pop_up(driver))
    #b.start()
    l.bad_login(driver)
    driver.get(url)
    l.bad_password(driver)
    driver.get(url)
    s.search_car_with_category(driver)
    driver.get(url)
    s.search_car_without_category(driver)
    driver.get(url)