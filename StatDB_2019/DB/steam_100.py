#!/usr/bin/env python

import sys

sys.path.append('/home/stat/anaconda3/lib/python37.zip')

sys.path.append('/home/stat/anaconda3/lib/python3.7')

sys.path.append('/home/stat/anaconda3/lib/python3.7/lib-dynload')

sys.path.append('/home/stat/anaconda3/lib/python3.7/site-packages')

import pymysql

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

import pandas as pd
from tqdm import tqdm_notebook

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("window-size=1920x1080")
options.add_argument("lang=ko_KR")
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2)'\
    'AppleWebKit/537.36 (KHTML, like Gecko)'\
    'Chrome/77.0.3865.120 Safari/537.36')

driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver', options = options)

# Top games by current player count
url = "https://store.steampowered.com/stats/"
driver.get(url)

try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'detailStats')))
    req = driver.page_source
finally:
    req = driver.page_source
driver.quit()

bs = BeautifulSoup(req, 'html.parser')
top_100 = bs.find('div', {'id': 'detailStats'}).findAll('tr', {'class': 'player_count_row'})


# DB connection
conn = pymysql.connect(host = "203.252.196.68",
                       user = 'db1614681', passwd = 'stat1234', db = 'sql1614681',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

top_100_list = []
for i in top_100:
    title = i.find('a').text
    cur_user = int(i.findAll('span')[0].text.replace(',',''))
    peak_user = int(i.findAll('span')[1].text.replace(',',''))

    query = """
                INSERT INTO cpt_top100 (TITLE, CUR_USER, PEAK_TODAY)
                VALUES (%s, %s, %s)
                ;
            """
    cur.execute( query, (title, cur_user, peak_user) )


conn.commit()
cur.close()
conn.close()