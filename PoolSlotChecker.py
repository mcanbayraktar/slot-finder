from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def check_available_slot():
  driver.get("https://online.spor.istanbul/uyegiris")
  username_field = driver.find_element(By.ID, "txtTCPasaport")
  password_field = driver.find_element(By.ID, "txtSifre")
  username_field.send_keys('EVENTHOUGHALLTHEHACKERSKNOWTURKISHCITIZENIDSISTILLCANNOTSHAREMINE')
  password_field.send_keys('LIKEISAIDABOVE:)')
  password_field.send_keys(Keys.RETURN)

  driver.get('https://online.spor.istanbul/uyespor')
  my_sessions = driver.find_element(By.ID, 'pageContent_rptListe_lbtnSeansSecim_0')
  my_sessions.click()

  element = driver.find_element(By.XPATH, "//select[@name='ctl00$pageContent$ddlBransFiltre']")
  all_options = element.find_elements(By.TAG_NAME, "option")
  for option in all_options:
    if option.get_attribute('value') == 'b0f372fd-28c4-4c7c-a797-f35b798bd44f': # the silly string referres to YÜZME
      option.click()
  
  all_slots = driver.find_elements(By.XPATH, "//div[@class='well']")

  slot_found = False
  for slot in all_slots:
    if ('rgb(8, 245, 26)' in slot.get_attribute('style')):
      slot_found = True
      print('ÇÖQQQQ')

  if (slot_found == False):
    print('BOŞ SLOT YOK PAMPA :/')

check_available_slot()

input("Press Enter to close the browser...")

driver.quit()