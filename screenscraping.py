from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Set up Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

# Navigate to the recipe page and extract recipe information
url = 'https://realfood.tesco.com/'
driver.get(url)

title = driver.find_element(By.XPATH, '//div[@class="recipe-detail"]/h1[@class="heading"]').text
description = driver.find_element(By.XPATH, '//div[@class="recipe-detail"]/p[@class="introduction"]').text
serving = driver.find_element(By.XPATH, '//div[@class="recipe-detail"]/p[@class="serving"]').text
time = driver.find_element(By.XPATH, '//div[@class="recipe-detail"]/p[@class="time"]').text
calories = driver.find_element(By.XPATH, '//div[@class="recipe-detail"]/p[@class="calories"]').text
ingredients_list = driver.find_element(By.XPATH, '//div[@class="recipe-detail"]/ul[@class="ingredients-list"]')
ingredients = [li.text for li in ingredients_list.find_elements(By.TAG_NAME, 'li')]

method_list = driver.find_element(By.XPATH, '//div[@class="recipe-detail"]/ol[@class="method-list"]')
method = [li.text for li in method_list.find_elements(By.TAG_NAME, 'li')]

# Print recipe information
print('Title:', title)
print('Description:', description)
print('Serving:', serving)
print('Time:', time)
print('Calories:', calories)
print('Ingredients:', ingredients)
print('Method:', method)

# Close Chrome driver
driver.quit()


