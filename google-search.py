# source: https://officeguide.cc/windows-python-selenium-automation-scripts-tutorial-examples/

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 使用 Chrome 的 WebDriver
browser = webdriver.Chrome()

# 開啟 Google 首頁
browser.get("https://www.google.com")

# 尋找網頁中的搜尋框
# inputElement = browser.find_element_by_name("q")
inputElement = browser.find_element(By.NAME, "q")

# 在搜尋框中輸入文字
inputElement.send_keys("Selenium")

# 送出搜尋
inputElement.submit()

# Google 搜尋結果的 XPath
resultLocator = "//a/h3/div"

try:
    # 等待網頁搜尋結果
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, resultLocator)))

    # 取得第一頁搜尋結果
    page1_results = browser.find_element(By.XPATH, resultLocator)

    print("results: ", page1_results)

    # 輸出搜尋結果
    for item in page1_results:
        print(item.text)

except TimeoutException:
    print('等待逾時！')