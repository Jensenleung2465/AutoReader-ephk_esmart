from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Install the Edge WebDriver
driver = webdriver.Edge()

# Log.function
def log_action(action):
    with open('automation_log.txt', 'a') as log_file:
        log_file.write(action + '\n')

# Main
def perform_tasks():
      # Step 1: Open the login page
      driver.get("https://ephchi.ephhk.com/readinggarden/index.php/login")
      log_action("Opened login page.")

      time.sleep(5)  # Wait for the page to load

      # Step 2: Click the button if it exists
      try:
          button = driver.find_element(By.CLASS_NAME, 'layui-layer-btn0')
          button.click()
          log_action("Clicked the button.")
      except Exception as e:
          log_action("Button not found: " + str(e))

      # Step 3: Input username
      username_input = driver.find_element(By.ID, "acc")
      username_input.send_keys("") #your esmart username 
      log_action("Entered username.")

        # Step 4: Input password
        password_input = driver.find_element(By.ID, "pwd")
        password_input.send_keys("") #your esmart password
        log_action("Entered password.")

        # Step 5: Click the login button
        login_button = driver.find_element(By.ID, "btn-login")
        login_button.click() #click button
        log_action("Clicked login button.")

        time.sleep(2)  # Wait for the next page to load

        #more function (send question to HomeWorkGPT - auto answer)

# run the tasks
perform_tasks()
