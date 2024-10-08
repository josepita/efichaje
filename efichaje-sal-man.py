# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestEntradaMaana():
  def setup_method(self, method):

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo sin cabeza
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    self.driver = webdriver.Chrome(options=chrome_options)

  def test_salidaMaana(self):
    self.driver.get("https://clientes.efichaje.com/efichaje")
    self.driver.set_window_size(1363, 1032)
    self.driver.find_element(By.ID, "M3").click()
    self.driver.find_element(By.ID, "M3").send_keys("44292186M")
    self.driver.find_element(By.ID, "M4").send_keys("yaestoydesalienado")
    self.driver.find_element(By.ID, "M10").click()
    self.driver.find_element(By.ID, "M28").click()
    self.driver.find_element(By.ID, "M28").click()
    self.driver.find_element(By.ID, "M28").send_keys("1400")
    self.driver.execute_script("arguments[0].value = '14:00';", self.driver.find_element(By.ID, "M28"))
    self.driver.find_element(By.ID, "M29").click()
    self.driver.find_element(By.ID, "M29").send_keys("Salida")
    self.driver.find_element(By.CSS_SELECTOR, "#M15 > img").click()
    self.driver.find_element(By.ID, "M53").click()
    self.driver.find_element(By.ID, "M7").click()
  
