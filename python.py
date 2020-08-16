from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#chrome_options = Options.add_argument("--headless")
import pdb
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://web.whatsapp.com")
pdb.set_trace()
driver.find_element_by_css_selector("[data-tab='3']").click()
driver.find_element_by_css_selector("[data-tab='3']").send_keys("information")

time.sleep(3)
driver.find_element_by_css_selector("div[role='option']").click()
driver.find_element_by_css_selector("div[data-tab='1']").send_keys("home")
driver.find_element_by_css_selector("span[data-testid='send']").click()
