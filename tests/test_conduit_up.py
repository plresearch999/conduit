from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import pathlib

# In order for ChromeDriverManager to work you must pip install it in your own environment.
browser_options = Options()
browser_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)

def test_conduit_up():
    driver.get("http://localhost:1667")
    time.sleep(5)
    driver.save_screenshot("screenshot.png")
    driver.quit()
    
    with open(pathlib.path("test.txt"), "w") as t:
        t.write('hello')
        
    with open(pathlib.path("test.txt"), "rt") as t:
        print(t.read())
