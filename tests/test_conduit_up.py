from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from pathlib import Path

# In order for ChromeDriverManager to work you must pip install it in your own environment.
browser_options = Options()
browser_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)

def test_conduit_up():
    driver.get("http://localhost:1667")
    time.sleep(5)
    driver.save_screenshot("screenshot.png")
    driver.quit()
    
    p = Path('.')
    print([x for x in p.iterdir() if x.is_dir()])
    
#     with open(Path("test.txt"), "w") as t:
#         t.write('hello')
        
#     with open(Path("test.txt"), "rt") as t:
#         print(t.read())

#     with open(Path("requirements.txt"), "rt") as t:
#         print(t.read())
