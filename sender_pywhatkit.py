import random

import pandas as pd
import math
from time import sleep
import pywhatkit
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send(area_code ,total_wait_time):
    total_wait_time = int(total_wait_time)

    for index, row in df.iterrows():
        tel_value = row['TEL']
        name_value = row['NAME']
        if not math.isnan(tel_value):
            tel_value = str(tel_value)
            pywhatkit.sendwhatmsg_instantly(area_code + tel_value, message, total_wait_time)
            sleep(total_wait_time+total_wait_time*0.25)


name=""
message = "test. "
filepath = "cn.xls"
df = pd.read_excel(filepath)

send("+549", 30)


