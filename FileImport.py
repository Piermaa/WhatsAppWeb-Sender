import pandas as pd
import math
from selenium import webdriver
from time import sleep
import pywhatkit
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send_message(telephone, webdriver):
    chat_finder = None

    while chat_finder is None:
        try:
            #chat_finder = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]")
            chat_finder = webdriver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        except NoSuchElementException:
            sleep(5)

    sleep(10) #WebDriverWait(webdriver, 10).until(
    # EC.prescence_of_element_located((By.ID, search_xpath))
    chat_finder.send_keys(tel_value)
    sleep(1)

    chat = webdriver.find_element(By.CLASS_NAME,"_3m_Xw").click()
    #chat = webdriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[5]/div/div/div")
    sleep(1)
    b = input("Continue")
    message_box = webdriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]")
    message_box.send_keys(message)
    send_button = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
    b = input("Continue")
    send_button.click()
    sleep(2)
#/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[2]/div/div

name=""
message = "test. "
filepath = "cn.xls"
df = pd.read_excel(filepath)

sleep(2)
webdriver = webdriver.Chrome()
webdriver.get("https://web.whatsapp.com/")
webdriver.maximize_window()

for index, row in df.iterrows():
    tel_value = row['TEL']
    name_value = row['NAME']
    message = message + name_value
    if not math.isnan(tel_value):
        tel_value = int(tel_value)
        send_message(tel_value, webdriver)