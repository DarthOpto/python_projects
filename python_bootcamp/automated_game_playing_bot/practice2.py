from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# navigate to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find anchor tag using CSS Selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search_input = driver.find_element(By.NAME, value="search")
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)
