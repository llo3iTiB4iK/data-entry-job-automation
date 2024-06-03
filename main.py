from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

anchors = soup.find_all('a', class_='StyledPropertyCardDataArea-anchor')
links = [anchor.get('href') for anchor in anchors]

prices = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
prices = [price.getText().split()[0].split('+')[0].split('/')[0] for price in prices]

addresses = soup.find_all('address')
addresses = [address.getText().strip().replace(" | ", " ") for address in addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(addresses)):
    driver.get("https://forms.gle/3GjgehQM9T6S9Tnu8")
    time.sleep(1)

    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])

    send_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_form.click()

driver.quit()
