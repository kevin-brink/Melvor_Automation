from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

url = "https://melvoridle.com/index.php"

def StartBrowser(url):
	driver = webdriver.Firefox()
	driver.get(url)
	driver.maximize_window()
	return driver

def SignIn(driver):
	# Click sign in

	#cloud_sign_in_button = driver.find_element_by_xpath("//button[contains(text(),'Sign In to Melvor Cloud')]")
	#cloud_sign_in_button.click()
	time.sleep(10)
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign In to Melvor Cloud')]"))).click()
	

	# Enter Username and password, hit Sign In

	#username_field = driver.find_element_by_id("cloud-login-form-username")
	#username_field.send_keys("Mitochondriak")
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cloud-login-form-username"))).send_keys("Mitochondriak")
	#password_field = driver.find_element_by_id("cloud-login-form-password")
	#password_field.send_keys("zomBie170!")
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cloud-login-form-password"))).send_keys("zomBie170!")

	#sign_in_button = driver.find_element_by_id("cloud-login-form-submit")
	#sign_in_button.click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cloud-login-form-submit"))).click()

	# Select first character
	#character = driver.find_element_by_id("character-select-0")
	#character.click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='character-selection-container']/button"))).click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "character-select-0"))).click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='swal2-confirm swal2-styled']"))).click()


def AutoLoot(driver):
	while True:
		time.sleep(30)

		while len(driver.find_elements_by_xpath("//div[@role='dialog']/div/button[contains(text(),'OK')]")) > 0:
			driver.find_element_by_xpath("//div[@role='dialog']/div/button[contains(text(),'OK')]").click()

		try:
			WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "combat-btn-loot-all"))).click()
		except:
			pass

	

def main(url):
	driver = StartBrowser(url)
	SignIn(driver)
	AutoLoot(driver)

main(url)