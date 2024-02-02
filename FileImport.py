import pandas as pd
import math
from selenium import webdriver
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_text_box_and_send(webdriver ,xpath, text):
    text_box = None
    while text_box is None:
        try:
            text_box = webdriver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(5)

    text_box.clear()
    text_box.send_keys(text)
    sleep(1)
    text_box.send_keys(Keys.ENTER)
    sleep(5)

def search_text_box_and_multi_send(webdriver ,xpath, texts):
    text_box = None
    while text_box is None:
        try:
            text_box = webdriver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(5)

    for text in texts:
        text_box.clear()
        text_box.send_keys(text)
        sleep(1)
        #text_box.send_keys(Keys.ENTER)
        sleep(1)
    sleep(5)

def send_message(telephone, webdriver, messages):
    try:
        search_text_box_and_send(webdriver, '//div[@contenteditable="true"][@data-tab="3"]', telephone)
        search_text_box_and_multi_send(webdriver, '//div[@contenteditable="true"][@title="Type a message"]', messages)

        print(f"Message sent to {telephone}")
    except Exception as e:
        print(f"Error sending message to {telephone}: {str(e)}")

contacts_load=True
name = ""
base_message1 = "TEST MSG: Hola @v1"
base_message2 = "TEST MSG: ARS @v2"
filepath = "cn.xls"
df = pd.read_excel(filepath)

sleep(2)
webdriver = webdriver.Chrome()
webdriver.get("https://web.whatsapp.com/")
webdriver.maximize_window()

for index, row in df.iterrows():
    tel_value = row['TEL']
    messages = [base_message1.replace("@v1", row['NAME']), base_message2.replace("@v2", str(row['AM']))]

    if not math.isnan(tel_value):
        tel_value = int(tel_value)
        send_message(tel_value, webdriver, messages)