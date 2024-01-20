from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def chrome_driver(silent=True):
  chrome_options = Options()

  if silent:
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--disable-blink-features=AutomationControlled")
  chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
  chrome_options.add_experimental_option("useAutomationExtension", False) 

  return webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

