import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ttkbootstrap import *


def search_text_box_and_send(driver, xpath, text):
    text_box = None
    tries = 0
    while text_box is None and (tries < 5):
        try:
            text_box = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            tries += 1
            sleep(5)

    if tries < 5:
        text_box.clear()
        text_box.send_keys(text)
        sleep(1)
        text_box.send_keys(Keys.ENTER)
        sleep(5)
        return text_box
    else:
        print(f"TIMEOUT EXCEPTION: COULD NOT FIND ELEMENT FOR XPATH: {xpath}")
        return None


def search_text_box_and_multi_send(driver, xpath, texts):
    text_box = None
    tries = 0
    while text_box is None and tries < 5:
        try:
            text_box = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(5)
            tries += 1

    if tries < 5:
        for text in texts:
            text_box.clear()
            text_box.send_keys(text)
            sleep(1)
            a=input("Send message? ")
            text_box.send_keys(Keys.ENTER)  # // LINE COMMENTED FOR TESTING     <-------------------------------------------
            sleep(1)
        sleep(5)
        return text_box
    else:
        print(f"TIMEOUT EXCEPTION: COULD NOT FIND ELEMENT FOR XPATH: {xpath}")
        return None


def send_message(telephone, driver, message):
    try:
        search_text_box_and_send(driver, '//div[@contenteditable="true"][@data-tab="3"]', telephone)
        # search_text_box_and_multi_send(webdriver, '//div[@contenteditable="true"][@title="Type a message"]', messages)
        message_box = search_text_box_and_send(driver, '//div[@contenteditable="true"][@data-tab="10"]', message)

        if message_box is not None:
            message_box.send_keys(Keys.ESCAPE)

        print(f"Message sent to {telephone}")

    except Exception as e:
        print(f"Error sending message to {telephone}: {str(e)}")


def replace_values(base_message: str, row):

    while '[' in base_message and ']' in base_message:
        # Find the first occurrence of '[' and ']'
        start_index = base_message.find('[')
        end_index = base_message.find(']')

        # Extract the substring within the square brackets
        placeholder = base_message[start_index + 1:end_index]


        # Check if the placeholder is a column in the Excel file
        if placeholder in row:
            # Get the value from the Excel file
            value = row[placeholder]

            # Replace the placeholder in the message with the value
            base_message = base_message[:start_index] + str(value) + base_message[end_index + 1:]
        else:
            print(f"Column '{placeholder}' not found in the Excel file.")

    return base_message


def send_messages(base_message):
    filepath = "cn.xlsx"
    df = pd.read_excel(filepath)

    sleep(2)
    web_driver = webdriver.Chrome()
    web_driver.get("https://web.whatsapp.com/")
    web_driver.maximize_window()

    # TIME FOR LOGIN AND CONTACTS LOAD
    sleep(30)

    for index, row in df.iterrows():
        tel_value = row['TEL']
     #   if tel_value == '' or tel_value == None:
     #       continue

        if not math.isnan(tel_value):
            tel_value = int(tel_value)
            message = replace_values(base_message, row)
            send_message(tel_value, web_driver, message)
