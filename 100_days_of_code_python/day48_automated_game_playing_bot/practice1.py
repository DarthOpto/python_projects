from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# # search_bar.send_keys("selenium")
# search_button = driver.find_element(By.ID, value="submit")
# # search_button.click()
# print(search_button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)
# submit_bug = driver.find_element(By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(submit_bug.text)

# Challenge: Print the event dates from python.org
event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_dates)):
    events[n] = {
        "time": event_dates[n].text,
        "name": event_names[n].text
    }

print(events)



# driver.close() closes the active tab
# driver.quit() closes the entire program
driver.quit()