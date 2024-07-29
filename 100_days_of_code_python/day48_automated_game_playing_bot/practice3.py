from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# navigate to appbrewery test
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Enter First Name
f_name_field = driver.find_element(By.NAME, value="fName")
f_name_field.send_keys("Curtis")

# Enter Last Name
l_name_field = driver.find_element(By.NAME, value="lName")
l_name_field.send_keys("Salisbury")

# Enter Email
email_field = driver.find_element(By.NAME, value="email")
email_field.send_keys("curtis.salisbury01@gmail.com")

# Click Sign Up button
sign_up_btn = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up_btn.click()