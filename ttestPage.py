import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_helper.pom import *
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope='module')
def browser():
    # 启动Chrome浏览器
    driver = webdriver.Chrome()
    # 打开指定页面
    driver.get('http://16.163.103.237:81/login')
    yield driver
    # 关闭浏览器
    driver.quit()


def test_open_page(browser):
    # 在打开的页面中查找指定元素
    browser.maximize_window()
    browser.find_element(By.XPATH, '//*[@id="username-login"]').send_keys('admin')
    browser.find_element(By.XPATH, '//*[@id="-password-login"]').send_keys('aA111111')
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/div['
                                   '3]/div/button').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/ul/div['
                                   '1]/div[2]/h6').click()
    time.sleep(2)
    browser.find_element(By.XPATH,
                         '//*[@id="root"]/div/nav/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/ul/div['
                         '2]/div/div/ul/a[1]/div/h6').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div[2]/div[3]/div[2]/div[1]/div[3]/button[2]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="username"]').send_keys('pytest001')
    browser.find_element(By.XPATH, '//*[@id="role"]').click()
    time.sleep(2)
    print(browser.find_element(By.XPATH, '//*[@id="menu-role_id"]/div[3]/ul/li[1]').text)
    print(browser.find_element(By.XPATH, '//*[@id="menu-role_id"]/div[3]/ul/li[2]').text)
    print(browser.find_element(By.XPATH, '//*[@id="menu-role_id"]/div[3]/ul/li[3]').text)
    browser.find_element(By.XPATH, '//*[@id="menu-role_id"]/div[3]/ul/li[1]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/form/div/div[2]/button[2]').click()
    time.sleep(2)
