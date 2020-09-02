from selenium import webdriver
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://instagram.com')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)

    def unsave_all(self):
        self.driver.get('https://instagram.com/{}/saved/'.format(self.username))
        sleep(1)
        href = self.driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a").get_attribute('href')
        self.driver.get(href)
        sleep(1)
        self.driver.find_element_by_xpath("//span[@class='wmtNn']/div/div/button").click()
        sleep(1)
        self.unsave_all()

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    my_bot = InstaBot(username, password)
    my_bot.unsave_all()

if __name__=='__main__':
    main()