from pyautogui import position,screenshot
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', value=True)

driver = webdriver.Chrome(options=chrome_option)

driver.get('https://elgoog.im/dinosaur-game/')
time.sleep(4)
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.SPACE)
try:
    while True:
        
        pixel_color = screenshot().getpixel((246, 630))
        
        if pixel_color == (83, 83, 83) or pixel_color == (172, 172, 172):
            body.send_keys(Keys.SPACE)


except KeyboardInterrupt:
    print("Stopped by user")
