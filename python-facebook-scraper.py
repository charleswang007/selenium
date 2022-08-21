# source: https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")
 
email = chrome.find_element(By.ID, "email")
password = chrome.find_element(By.ID, "pass")
 
email.send_keys('example@gmail.com') # email
password.send_keys('*****') # password
password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')

# time.sleep(5)
# chat = chrome.find_element_by_css_selector(
#     '.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hnxzwevs.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l')
# chat.click()

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

soup = BeautifulSoup(chrome.page_source, 'html.parser')

titles = soup.find_all('div', {
    'class': 'm8h3af8h l7ghb35v kjdc1dyq kmwttqpk gh25dzvf n3t5jt4f'})

for title in titles:
    post = title.find('div', {'dir': 'auto'})
    if post:
        print(post.getText())
 
chrome.quit()