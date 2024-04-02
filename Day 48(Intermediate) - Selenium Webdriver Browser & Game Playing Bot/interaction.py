from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
# driver.close()


all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search") #searching a elemnt 
search.send_keys("Python") #typing text into the input element
search.send_keys(Keys.ENTER) #pressing enter

# 1. Import and Setup Selinum and Webdriver
# 2. Get the link of the website that we want to interact
# 3. find elemnts and interact with the website
# 4. Close the website driver
