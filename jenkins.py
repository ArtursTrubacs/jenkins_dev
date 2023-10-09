from selenium import webdriver
import time

# Create ChromeOptions and set headless mode and window size
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')

# Initialize the Selenium WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the URL
driver.get("https://www.jenkins.io/")

# Wait for 4 seconds (you can use WebDriverWait for more precise waits)
time.sleep(4)

# Get and print the title of the page
title = driver.title
print("Title of the page:", title)

# Close the browser
driver.quit()
