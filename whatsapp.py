# sending umknown numbes......2 numbers checked

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\suraj\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://web.whatsapp.com/")


with open('groups.txt', 'r', encoding= 'utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding= 'utf8') as f:
    msg = f.read()


def send_unsaved_contact_message():
    time.sleep(10)
    driver.implicitly_wait(10)
    input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    pyperclip.copy(msg)
    input_box.send_keys(Keys.CONTROL + "v")  # 
    input_box.send_keys(Keys.ENTER)

    time.sleep(2)

for group in groups:
    link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(group)
            # driver  = webdriver.Chrome()
    driver.get(link)
    send_unsaved_contact_message()