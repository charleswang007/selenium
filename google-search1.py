# source: https://matters.news/@CHWang/90524-coding%E8%B5%B7%E4%BE%86-python%E8%87%AA%E5%8B%95%E5%8C%96%E7%88%AC%E8%9F%B2-selenium%E5%A5%97%E4%BB%B6-%E6%96%B9%E6%B3%95%E6%95%99%E5%AD%B8-bafyreieq5sbozlrboqb42eg2yu3q6vrtqshjbuztq6xiy4tiz3d4sxydzm

## Import Package
from pyrsistent import v
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

## 啟用Options方法
options = Options()
## 關掉通知
options.add_argument(" - disable-notifications")
## WebDriver Path
webdriver_path = "./chromedriver"
## Enabled Chrome function
chrome_browser = webdriver.Chrome(executable_path = webdriver_path)
## go to the website
chrome_browser.get("https://www.google.com/")
## 獲得搜尋欄的元素
search = chrome_browser.find_element(By.NAME, "q")
## 傳入文字
search.send_keys("coding起來")
## 延遲時間
time.sleep(2)
## 獲得按鈕元素並觸發點擊事件
search.submit()