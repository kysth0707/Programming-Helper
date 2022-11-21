from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip
import json
from pyautogui import hotkey
import time
from datetime import datetime
import math


def FindAndClick(selector : str):
	driver.find_element(By.CSS_SELECTOR, selector).click()



WebURLS = None
with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\WebURLS.json", mode="r") as f:
	WebURLS = json.loads("".join(f.readlines()))

UserDatas = None
with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\UserDatas.json", mode="r") as f:
	UserDatas = json.loads("".join(f.readlines()))


# LOGIN
driver = webdriver.Chrome("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\chromedriver.exe")
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
def GetPageURL(page):
	return str(WebURLS["TargetURL"]).replace('{num}', f'{page}')

driver.get(GetPageURL(1))

Wait = WebDriverWait(driver, 10)
Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, WebURLS['PageSelector'])))

time.sleep(1)

ContentCount = driver.find_element(By.CSS_SELECTOR, WebURLS['ContentCount']).text
ContentCount = int(str(ContentCount).replace(",",""))
print(f"게시물 수 : {ContentCount}")

def GetContents(Num, IndexNum):
	"""
	Num Starts at 1
	----------
	"""
	
	SearchTop = str(WebURLS['ContentSelector']).replace("{num}", f"{Num}")

	Header = False

	try:
		# #app > div > div.article-board.article_profile > table > tbody > tr:nth-child(1) > td.td_article > div.board-list > div > a.article
		ContentTitle = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a.article").text)
		try:
			Header = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a.article > span").text)
		except:
			pass
	except:
		ContentTitle = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a").text)
		try:
			Header = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a > span").text)
		except:
			pass
	ContentID = driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-number > div").text
	try:
		ContentCommentCount = driver.find_element(By.CSS_SELECTOR, f"{SearchTop}  > td.td_article > div.board-list > div > a.cmt > em").text
	except:
		ContentCommentCount = 0
	ContentDate = driver.find_element(By.CSS_SELECTOR, f"{SearchTop}  > td.td_date").text
	ContentView = driver.find_element(By.CSS_SELECTOR, f"{SearchTop}  > td.td_view").text

	return {
			"Index" : IndexNum,
			"Header" : Header,
			"ContentTitle" : ContentTitle, 
			"ContentID" : ContentID, 
			"ContentCommentCount" : ContentCommentCount, 
			"ContentDate" : ContentDate, 
			"ContentView" : ContentView
			}

PageCount = math.ceil(ContentCount / 15)

Output = {
		  "ContentCount" : ContentCount, 
		  "PageCount" : PageCount, 
		  "CheckedDate" : str(datetime.now())
		  }
Data = []

EstimatedTime = time.time()

Index = 0
for CurrentPage in range(PageCount - 1):
	# FindAndClick(str(WebURLS['PageSelector']).replace('{num}', f'2'))
	print(f'{CurrentPage + 1} / {PageCount} | {(CurrentPage + 1)/PageCount * 100}%')

	for i in range(10):
		try:
			Data.append(GetContents(1 + i, Index))
		except Exception as e:
			print(e)
			print(Index, CurrentPage + 1)
		Index += 1

	driver.get(GetPageURL(CurrentPage + 2))
	Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, str(WebURLS['ContentSelector']).replace("{num}", "1"))))

	if CurrentPage == 0:
		EstimatedTime = (time.time() - EstimatedTime) / 15 * ContentCount
		print(f'예상 시간 : {EstimatedTime//60} 분 {EstimatedTime%60} 초')

for i in range(ContentCount % 15):
	Data.append(GetContents(1 + i, Index))
	Index += 1

Output["Data"] = Data

with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\Output.json", "w", encoding="utf-8") as f:
	json.dump(Output, f, ensure_ascii=False, indent=4)

# #app > div > div.article-board.article_profile > table > tbody > tr:nth-child(1)
# #app > div > div.article-board.article_profile > table > tbody > tr:nth-child(1) > td.td_article > div.board-list > div > a.article
# #app > div > div.article-board.article_profile > table > tbody > tr:nth-child(1) > td.td_article > div.board-list > div > a.article