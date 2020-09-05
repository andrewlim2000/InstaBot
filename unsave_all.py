from selenium import webdriver
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = None

def sign_in(username, password):
    global driver
    driver = webdriver.Chrome(PATH)
    driver.get('https://instagram.com')
    sleep(2)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(2)

def unsave_all(username):
    global driver
    driver.get('https://instagram.com/{}/saved/'.format(username))
    sleep(1)
    href = driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a").get_attribute('href')
    driver.get(href)
    sleep(1)
    driver.find_element_by_xpath("//span[@class='wmtNn']/div/div/button").click()
    unsave_all(username)

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    sign_in(username, password)
    unsave_all(username)

if __name__=='__main__':
    main()