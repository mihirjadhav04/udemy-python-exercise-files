from selenium import webdriver

# from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
event_time = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")
for time in event_time:
    print(time.text)

for name in event_name:
    print(name.text)

events = {}

for n in range(len(event_time)):
    events[n] = {"time": event_time[n].text, "name": event_name[n].text}
    # print(events)

print(events)


# print(event_data)
driver.close()
