from selenium import webdriver                                    # Import WebDriver für Zugriff auf URL
import time                                                       # Import Time-Library für Verzögerungen wenn notwendig
from selenium.webdriver.common.keys import Keys                   # Import Keys to send Key-strokes
driver = webdriver.Chrome(os.getcwd() + '/chromedriver')          # Driver für Chrome definieren - mit akt. Ordner os.getcwd
driver.get("url")
