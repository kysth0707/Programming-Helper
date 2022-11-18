# from selenium import webdriver
# from selenium.webdriver.common.by import By

# import pyperclip
# import json
# from pyautogui import hotkey
# import time
import math


# def FindAndClick(selector : str):
# 	driver.find_element(By.CSS_SELECTOR, selector).click()



# WebURLS = None
# with open("WebURLS.json", mode="r") as f:
# 	WebURLS = json.loads("".join(f.readlines()))

# UserDatas = None
# with open("UserDatas.json", mode="r") as f:
# 	UserDatas = json.loads("".join(f.readlines()))


# # LOGIN
# driver = webdriver.Chrome("chromedriver.exe")
# driver.get(WebURLS["Login"])

# pyperclip.copy(UserDatas["ID"])
# FindAndClick("#id")
# time.sleep(0.1)
# hotkey("ctrl", "v")

# pyperclip.copy(UserDatas["PW"])
# FindAndClick("#pw")
# time.sleep(0.1)
# hotkey("ctrl", "v")
# time.sleep(0.1)
# hotkey("enter")


# # Move To Cafe
# driver.get(WebURLS["Cafe"])
# driver.implicitly_wait(10)
# FindAndClick("#cafe-info-data > ul > li.tit-action > p > a")
# time.sleep(0.5)
# FindAndClick("#ia-action-data > div.ia-info-data3 > ul > li.info2 > span > strong > a")
# time.sleep(1)
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#cafe_main"))
# time.sleep(1)

# ContentCount = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/span[2]/em').text
# ContentCount = int(str(ContentCount).replace(",",""))
# print(f"게시물 수 : {ContentCount}")

ContentCount = 1206

ContentsPerPage = 15

LastPageContentCount = ContentCount % ContentsPerPage
print(LastPageContentCount)
PageCount = math.ceil(ContentCount / ContentsPerPage)

WantToFindNum = 1206


WantToFindPage = (PageCount - ((WantToFindNum - LastPageContentCount) // 15))

print(WantToFindPage)


# for i in range(WantToFindPage // 10):
# 	time.sleep(1)
# 	FindAndClick("#app > div > div.paginate_area > div > button.btn.type_next") #next page

# time.sleep(1)
# if WantToFindPage % 10 == 1:
# 	FindAndClick(f"#app > div > div.paginate_area > div > button:nth-child({WantToFindPage % 10 + 1})")
# else:
# 	FindAndClick(f"#app > div > div.paginate_area > div > button:nth-child({WantToFindPage % 10 + 2})")
# time.sleep(10)
