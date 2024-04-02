# This webdriver is responsible for driving and automating our tasks on web browser.
from selenium import webdriver


chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# .get method open a new window with the specified url
driver.get(
    "https://www.amazon.in/dp/B07BRKK9JQ/ref=s9_acsd_al_bw_c2_x_2_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=ZJ3GS9E52A2HYC49EDBJ&pf_rd_t=101&pf_rd_p=a97a0da3-9aa6-46f7-80ec-5410f591172a&pf_rd_i=1375248031&th=1"
)

# price = driver.find_element_by_class_name("a-price")
# driver.find_element_by_id(id_)
# driver.find_element_by_css_selector(css_selector)
# driver.find_element_by_name(name)


print(price.text)
# to close the window - 1 tab
driver.close()
