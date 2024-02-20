from PIL import Image
import pyperclip
import io

import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ttkbootstrap import *
import pyperclip
from MessageRedaction import *
import shutil
import WhatsAppMessage

def copy_to_clipboard(filepath):
    try:
        with open(filepath, 'rb') as image_file:
            image_data = io.BytesIO(image_file.read())
            img = Image.open(image_data)

            # Convert the image to RGBA format (if not already in RGBA)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')

            # Convert the image to bytes
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes.seek(0)

            # Copy the image bytes to clipboard using pyperclip
            pyperclip.copy(str(img_bytes.read()))

            print(f"Image '{filepath}' copied to clipboard successfully.")
    except FileNotFoundError:
        print(f"Error: Image '{filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

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


def search_text_box_and_multi_send(driver, xpath, messages):
    text_box = None
    tries = 0
    while text_box is None and tries < 5:
        try:
            text_box = driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            sleep(5)
            tries += 1

    if tries < 5:
        for message in messages:
            text_box.clear()

            if message.filepath != '':
                copy_to_clipboard(message.filepath)
                sleep(1)
                text_box.send_keys(Keys.CONTROL, "v")
                sleep(5)

            text_box.send_keys(message.base_text)
            sleep(1)
            a = input("Send message? ")
            text_box.send_keys(Keys.ENTER)  # // LINE COMMENTED FOR TESTING     <-------------------------------------------
            sleep(1)
        sleep(5)
        return text_box
    else:
        print(f"TIMEOUT EXCEPTION: COULD NOT FIND ELEMENT FOR XPATH: {xpath}")
        return None


def send_message(telephone, driver, messages):
    try:
        search_text_box_and_send(driver, '//div[@contenteditable="true"][@data-tab="3"]', telephone)

        message_box = search_text_box_and_multi_send(driver, '//div[@contenteditable="true"][@data-tab="10"]', messages)

        if message_box is not None:
            message_box.send_keys(Keys.ESCAPE)

        print(f"Message sent to {telephone}")

    except Exception as e:
        print(f"Error sending message to {telephone}: {str(e)}")


def send_messages(base_messages, excel_filepath, telephone_numbers_column):
    filepath = excel_filepath
    df = pd.read_excel(filepath)

    sleep(2)
    web_driver = webdriver.Chrome()
    web_driver.get("https://web.whatsapp.com/")
    web_driver.maximize_window()

    # TIME FOR LOGIN AND CONTACTS LOAD
    sleep(30)

    for index, row in df.iterrows():
        tel_value = row[telephone_numbers_column]

        if not math.isnan(tel_value):
            tel_value = int(tel_value)
            messages = replace_values(base_messages, row)
            send_message(tel_value, web_driver, messages)
