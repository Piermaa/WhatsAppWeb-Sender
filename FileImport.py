import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ttkbootstrap import *


def search_text_box_and_send(driver, xpath, text):
    text_box = None
    while text_box is None:
        try:
            text_box = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(5)

    text_box.clear()
    text_box.send_keys(text)
    sleep(1)
    text_box.send_keys(Keys.ENTER)
    sleep(5)


def search_text_box_and_multi_send(driver, xpath, texts):
    text_box = None
    while text_box is None:
        try:
            text_box = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(5)

    for text in texts:
        text_box.clear()
        text_box.send_keys(text)
        sleep(1)
        # text_box.send_keys(Keys.ENTER)  // LINE COMMENTED FOR TESTING     <-------------------------------------------
        sleep(1)
    sleep(5)


def send_message(telephone, driver, message):
    try:
        search_text_box_and_send(driver, '//div[@contenteditable="true"][@data-tab="3"]', telephone)
        # search_text_box_and_multi_send(webdriver, '//div[@contenteditable="true"][@title="Type a message"]', messages)
        search_text_box_and_send(driver, '//div[@contenteditable="true"][@title="Type a message"]', message)
        print(f"Message sent to {telephone}")
    except Exception as e:
        print(f"Error sending message to {telephone}: {str(e)}")


def get_replace_values(values_amount, rows):
    values = []
    for i in range(values_amount):
        values.append(rows["v" + str(i+1)])
    return values


def replace_values(base_message: str, values_amount: int, rows):
    message = base_message
    values = get_replace_values(values_amount, rows)

    for i in range(len(values)):
        message = message.replace("@v" + str(i+1), str(values[i]))

    return message


def send_messages(base_message, values_amount):
    filepath = "cn.xls"
    df = pd.read_excel(filepath)

    sleep(2)
    web_driver = webdriver.Chrome()
    web_driver.get("https://web.whatsapp.com/")
    web_driver.maximize_window()

    # TIME FOR LOGIN AND CONTACTS LOAD
    sleep(10)

    for index, row in df.iterrows():
        tel_value = row['TEL']

        if not math.isnan(tel_value):
            tel_value = int(tel_value)
            message = replace_values(base_message, values_amount, row)
            send_message(tel_value, web_driver, message)
