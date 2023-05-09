from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def process_recipe(driver: Chrome, url: str) -> dict:
	output = {
		"title": "",
		"description": "",
		"serving": "",
		"time": "",
		"calories": "",
		"ingredients": [],
		"method": [],
		"promo_links": []
	}

	# Go to the recipe url
	driver.get(url)

	if "search.php" in driver.current_url:
		output["title"] = "Error"
		output["promo_links"] = [x.get_attribute("href") for x in driver.find_elements(By.CLASS_NAME, "ddl-search-results__item-link")]
		return output

	output["title"] = driver.find_element(By.CLASS_NAME, 'recipe-detail__headline').text
	output["description"] = driver.find_element(By.CLASS_NAME, 'recipe-detail__intro').text
	output["serving"] = driver.find_element(By.CLASS_NAME, 'recipe-detail__meta-item_servings').text
	output["time"] = driver.find_element(By.CLASS_NAME, 'recipe-detail__meta-item_time').text
	output["calories"] = driver.find_element(By.CLASS_NAME, 'recipe-detail__meta-item_calories').text
	ingredients_list = driver.find_element(By.ID, "recipeingredients").find_element(By.CLASS_NAME,"recipe-detail__list")
	output["ingredients"] = [x.text for x in ingredients_list.find_elements(By.CLASS_NAME, "recipe-detail__list-item")]

	method_list = driver.find_element(By.ID, "method").find_element(By.CLASS_NAME, "recipe-detail__cms").find_element(By.TAG_NAME, "ol")
	output["method"] = [x.text for x in method_list.find_elements(By.TAG_NAME, "li")]

	promo_list = driver.find_element(By.CLASS_NAME, "recipe-detail__promo-list")

	output["promo_links"] = [x.find_element(By.TAG_NAME, "a").get_attribute("href") for x in promo_list.find_elements(By.TAG_NAME, "lI")]


	return output