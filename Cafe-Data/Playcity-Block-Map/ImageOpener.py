from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request as req

import pyperclip
import json
from pyautogui import hotkey
import time
from datetime import datetime
import math


def FindAndClick(selector : str):
	driver.find_element(By.CSS_SELECTOR, selector).click()



WebURLS = None
with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\Playcity-Block-Map\\WebURLS.json", mode="r") as f:
	WebURLS = json.loads("".join(f.readlines()))

UserDatas = None
with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\Playcity-Block-Map\\UserDatas.json", mode="r") as f:
	UserDatas = json.loads("".join(f.readlines()))


# LOGIN
driver = webdriver.Chrome("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\Playcity-Block-Map\\chromedriver.exe")
driver.get(WebURLS["Login"])

pyperclip.copy(UserDatas["ID"])
FindAndClick("#id")
time.sleep(0.1)
hotkey("ctrl", "v")

pyperclip.copy(UserDatas["PW"])
FindAndClick("#pw")
time.sleep(0.1)
hotkey("ctrl", "v")
time.sleep(0.1)
hotkey("enter")


# Move To Cafe

# Wait = WebDriverWait(driver, 10)

Links = None
with open(r'E:\GithubProjects\Programming-Helper\Cafe-Data\Playcity-Block-Map\Output.json', mode="r") as f:
	Links = json.loads("".join(f.readlines()))
for i in range(192, len(Links['Data'])):
	ContentID = Links['Data'][i]['ContentID']
	Link = f"https://cafe.naver.com/playct/{ContentID}"
	driver.get(Link)
	# Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div > div > div.ArticleContentBox > div.article_header > div.ArticleTool > a.button_url")))
	time.sleep(2.5)
	print(i, Link)

	content = driver.find_element(By.CSS_SELECTOR, "#cafe_main")
	driver.switch_to.frame(content)

	Title = driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.ArticleContentBox > div.article_header > div.ArticleTitle > div > h3").text
	if Title[:10] != "블록서버 전체 지도":
		continue

	Contents = driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div//*')

	ImageURL = ''
	for content in Contents:
		if content.get_attribute('src') != None:
			ImageURL = content.get_attribute('src')
			break

	req.urlretrieve(ImageURL, fr'E:\GithubProjects\Programming-Helper\Cafe-Data\Playcity-Block-Map\imgs\{i}.png')
	# exit()
	# break

	# driver.execute_script(f'window.open("{Link}");')