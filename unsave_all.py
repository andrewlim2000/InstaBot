from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = None

def sign_in(username, password):
    global driver
    driver = webdriver.Chrome()
    driver.get('https://instagram.com')
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(10)

def unsave_all(username):
    global driver
    driver.get('https://instagram.com/{}/saved/all-posts/'.format(username))
    sleep(2)
    href = driver.find_element(By.XPATH, "//div[@class='_aabd _aa8k _aanf']/a").get_attribute('href')
    driver.get(href)
    sleep(2)
    driver.find_element(By.XPATH, "//span[@class='_aamz']/div/div/button").click()
    unsave_all(username)

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    sign_in(username, password)
    unsave_all(username)

if __name__=='__main__':
    main()