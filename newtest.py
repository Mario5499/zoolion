import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1345x610")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1354, 610)
actions = ActionChains(driver)
print("script started")

driver.get("https://rrkb.in.net/code/Pytho_code_8.html")
print("Done")
print("done")


driver.quit()
