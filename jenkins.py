from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 # Use Chrome as an example

# Create a WebDriver instance using WebDriver Manager to manage the driver version
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the Jenkins page
driver.get('https://your-jenkins-url.com')  # Replace with your Jenkins URL

# Optional: Perform actions on the Jenkins page
# ...

# Close the browser
driver.quit()
