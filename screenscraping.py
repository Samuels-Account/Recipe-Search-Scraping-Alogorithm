from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Set up Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

# Navigate to the home page
url = 'https://realfood.tesco.com/'
driver.get(url)

links = set()

recipes = [x.get_attribute("href") for x in driver.find_elements(By.CLASS_NAME, "hp-grid-carousel__link")]

recipes2 = [x for x in recipes if x.startswith(url + "recipes/")]

links.add(recipes2[0])

print(links)



# Close Chrome driver
driver.quit()


