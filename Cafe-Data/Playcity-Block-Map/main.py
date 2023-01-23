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
def GetPageURL(page):
	return str(WebURLS["TargetURL"]).replace('{num}', f'{page}')

driver.get(GetPageURL(1))

# Wait = WebDriverWait(driver, 10)
# Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, WebURLS['WaitUntil'])))
print("드갑니다")

time.sleep(1)

def GetContents(Num, IndexNum):
	"""
	Num Starts at 1
	----------
	"""
	
	# SearchTop = str(WebURLS['ContentSelector']).replace("{num}", f"{Num}")
	SearchTop = f"#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child({Num}) > td.td_article > div.board-number > div"

	# Header = False

	# try:
	# 	ContentTitle = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a.article").text)
	# 	try:
	# 		Header = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a.article > span").text)
	# 	except:
	# 		pass
	# except:
	# 	ContentTitle = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a").text)
	# 	try:
	# 		Header = str(driver.find_element(By.CSS_SELECTOR, f"{SearchTop} > td.td_article > div.board-list > div > a > span").text)
	# 	except:
	# 		pass
	ContentID = driver.find_element(By.CSS_SELECTOR, SearchTop).text
	# try:
	# 	ContentCommentCount = driver.find_element(By.CSS_SELECTOR, f"{SearchTop}  > td.td_article > div.board-list > div > a.cmt > em").text
	# except:
	# 	ContentCommentCount = 0
	# ContentDate = driver.find_element(By.CSS_SELECTOR, f"{SearchTop}  > td.td_date").text
	# ContentView = driver.find_element(By.CSS_SELECTOR, f"{SearchTop}  > td.td_view").text

	return {
			"Index" : IndexNum,
			# "Header" : Header,
			# "ContentTitle" : ContentTitle, 
			"ContentID" : ContentID, 
			# "ContentCommentCount" : ContentCommentCount, 
			# "ContentDate" : ContentDate, 
			# "ContentView" : ContentView
			}

Output = {
		  "CheckedDate" : str(datetime.now())
		  }
Data = []


EstimatedTime = time.time()

Index = 1
PageNum = 1
Run = True
while Run:
	content = driver.find_element(By.CSS_SELECTOR, "#cafe_main")

	driver.switch_to.frame(content)
	# driver.get(GetPageURL(PageNum))
	# print(f'{CurrentPage + 1} / {PageCount} | {(CurrentPage + 1)/PageCount * 100}%')

	for i in range(15):
		try:
			Data.append(GetContents(1 + i, Index))
		except Exception as e:
			print(e)
			# print(Index, CurrentPage + 1)
			Run = False
			break
		Index += 1


	try:
		PageNum += 1
		driver.get(GetPageURL(PageNum))
		# Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, str(WebURLS['WaitUntil']))))
		time.sleep(2)
	except Exception as e:

		Run = False
		break

Output["Data"] = Data

with open("E:\\GithubProjects\\Programming-Helper\\Cafe-Data\\Playcity-Block-Map\\Output.json", "w", encoding="utf-8") as f:
	json.dump(Output, f, ensure_ascii=False, indent=4)