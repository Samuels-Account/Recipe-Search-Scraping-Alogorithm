from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from processrecipe import process_recipe
import random

NUM_LINKS = 25 # Number of total links to crawl. Links will be obtained from each crawled page
LINKS_PER_CRAWL = 2 # How many related links to store from each page

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
links = []

recipes = [x.get_attribute("href") for x in driver.find_elements(By.CLASS_NAME, "hp-grid-carousel__link")]

recipes2 = [x for x in recipes if x.startswith(url + "recipes/")]

links.append(random.choice(recipes2))

print("Links found!")

recipeInfo = []

i = 0
failed_parses = 0
while i < len(links):
	print(f"Processing recipe {i+1}/{NUM_LINKS + failed_parses}...")
	try:
		recipe = process_recipe(driver, links[i])
	except:
		i += 1
		failed_parses += 1
		continue
	if recipe["title"] != "Error":
		recipeInfo.append(recipe)
		if len(recipeInfo) >= NUM_LINKS:
			break
	else:
		print("Recipe not found")

	ls = list(recipe["promo_links"])
	j = 0
	while j < LINKS_PER_CRAWL:
		randoms = random.choice(ls)
		links.append(randoms)
		ls.remove(randoms)
		j += 1

	i += 1

TABLE_NAME = "Recipes" # Table to write values to
STARTING_ID = 25 # ID to start the RecipeID column at, this needs to be set correcly before and after every use

with open("recipes.sql", "w") as file:
	for recipe in recipeInfo:
		file.write("INSERT INTO `{}` VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\");\n".format(TABLE_NAME, STARTING_ID, recipe["title"], recipe["description"], recipe["serving"], recipe["time"], recipe["calories"], "%%%".join(recipe["ingredients"]), "%%%".join(recipe["method"]).strip("\n")))
		STARTING_ID += 1

# Close Chrome driver
driver.quit()

print("STARTING_ID Incremented to " + str(STARTING_ID))


