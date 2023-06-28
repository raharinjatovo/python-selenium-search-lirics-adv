from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import dotenv
import time
dotenv.load_dotenv('.env')
import os

# Load Facebook credentials from environment variables
facebook_email = os.environ.get('FacebookEmail')
facebook_password = os.environ.get('FacebookPassword')

# Path to your Chrome WebDriver executable
webdriver_path = './chromedriver.exe'

# Group URL and search query
group_url = 'https://web.facebook.com/groups/727098127408374'
search_query = 'Your search query'

# Create a WebDriver instance with the desired user agent
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(webdriver_path), options=options)

# Navigate to Facebook
driver.get('https://www.facebook.com')

# Find and fill in the login form
wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
password_input = driver.find_element(By.NAME, 'pass')
email_input.send_keys(facebook_email)
password_input.send_keys(facebook_password)
password_input.submit()

# Wait for the homepage to load
driver.implicitly_wait(10)

# Navigate to the Facebook group
driver.get(group_url)

# Wait for the group page to load
driver.implicitly_wait(10)

# Find the search input and enter the search query
# search_input = driver.find_element(By.CLASS_NAME, 'x1b0d499')
# search_input.click()

# Find the container <div> by its attributes
container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Rechercher')))


# Find and click the first child element of the container
first_child_element = container.find_element(By.XPATH, './child::*[1]')
first_child_element.click()
input_search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Rechercher dans ce groupe')))
input_search.send_keys('ambasadora ilay feo')
input_search.send_keys(Keys.RETURN)
# Wait for the search results to load
time.sleep(120)

# Perform further actions on the search results if needed

# Close the browser
driver.quit()
