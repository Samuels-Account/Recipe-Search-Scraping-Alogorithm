from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from processrecipe import process_recipe
import random

NUM_LINKS = 5

print("Warming up Selenium...")
# Set up Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

# Navigate to the home page
url = 'https://realfood.tesco.com/'
print(f"Accessing \"{url}\"...")
driver.get(url)

print("Searching for promo links...")
links = set()

recipes = [x.get_attribute("href") for x in driver.find_elements(By.CLASS_NAME, "hp-grid-carousel__link")]

recipes2 = [x for x in recipes if x.startswith(url + "recipes/")]

links.add(recipes2[0])

print("Links found!")

recipeInfo = []

i = 0
while i < len(links):
	print(f"Processing recipe {i+1}/{NUM_LINKS}...")
	recipe = process_recipe(driver, list(links)[i])
	if recipe["title"] != "Error":
		recipeInfo.append(recipe)
		if len(recipeInfo) >= NUM_LINKS:
			break
	for link in recipe["promo_links"]:
		if not link in links and random.randint(0,1) == 1:
			links.add(link)
			break

	i += 1

# Close Chrome driver
driver.quit()


