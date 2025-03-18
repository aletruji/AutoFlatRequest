from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_selenium():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Optional: Headless-Modus aktivieren
    # chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.google.com")
    print("Google geöffnet")
    driver.quit()

if __name__ == "__main__":
    test_selenium()