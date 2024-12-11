from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Para buscar un elemento
driver.find_element(By.CSS_SELECTOR, ".auth-form__title")

driver.quit()