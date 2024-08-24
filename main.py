import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import secrets

url = "https://myalice-automation-test.netlify.app/"
print("[+] Starting . . . .")

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,20)
driver.get(url)






def login(driver):
    # Login with username and password
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("testuser")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    driver.find_element(By.XPATH, '//*[@id="login-btn"]').click()
    time.sleep(5)



def search(driver):

# Search term Naruto
    
    search_box = driver.find_element(By.XPATH, '//*[@id="manga-search"]')
    new_text = "Naruto"
    search_box.send_keys(new_text)
    
    driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
    time.sleep(5)

# Search term One piece

    search_box.clear()
    
    new_text = "One piece"
    search_box.send_keys(new_text)
    
    driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
    time.sleep(5)

# Search term Seven Deadly Sins (No magna found)

    search_box.clear()
    new_text = "Seven Deadly Sins"
    search_box.send_keys(new_text)
    driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
    time.sleep(5)
    

# Search term No results

    search_box.clear()
    new_text = "sfgdgfh"
    search_box.send_keys(new_text)
    driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
    time.sleep(5)
    



    






def main(driver):

    login(driver)
    search(driver)
    




if __name__ == "__main__":
    main(driver)








