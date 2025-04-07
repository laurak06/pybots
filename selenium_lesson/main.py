import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def is_login():
    driver.get('https://github.com/login')
    login = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#login_field'))
    )

    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))
    )

    btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button'))
    )

    login.send_keys('laurak06')
    password.send_keys('Zxc,vb,123')
    btn.click()

    time.sleep(3)

    new_rep = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive.full-width > div.application-main > div > div > aside > div > div > loading-context > div > div.Details.js-repos-container.mt-5 > div > div.hide-sm.hide-md.mb-1.d-flex.flex-justify-between.flex-items-center > a > span'))
    )
    new_rep.click()

    time.sleep(3)

    rep_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#\:r5\:'))
    )

    rep_desc = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#\:ra\:'))
    )

    rep_name.send_keys('new_selenium_rep')
    rep_desc.send_keys('описание')

    create_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive > div.application-main > main > react-app > div > form > div.Box-sc-g0xbh4-0.dlBivO > button > span > span'))
    )

    create_btn.click()
    time.sleep(3)


is_login()
driver.quit()