import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url="https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url)


if response.status_code==200:
    soup = BeautifulSoup(response.text, 'html.parser')

    prices= soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
    addresses=soup.find_all("address")
    links = soup.find_all("a", class_="property-card-link")

    price_list = [price.get_text().replace("/mo", "").split("+")[0] for price in prices]
    add_list=[add.get_text().replace("\n", "").replace("|", "").strip() for add in addresses]
    link_list=[link.get("href") for link in links]

    # print(len(price_list))
    # print(len(add_list))
    # print(len(link_list))

else:
    print("failed")

slice_price=price_list[2: 5]
slice_add=add_list[2: 5]
slice_link=link_list[2: 5]
# print(len(slice_price))
# print(len(slice_add))
# print(len(slice_link))


chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome)

driver.get("https://forms.gle/pi4c14944E2M3he87")
wait=WebDriverWait(driver, 10)

i=0
while i<=len(slice_add)-1:
    # address=wait.until(EC.element_to_be_clickable((By.XPATH, '')))
    address=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(slice_add[i])
    price=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(slice_price[i])
    link=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(slice_link[i])
    submit=driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit.click()
    another_response=driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    another_response.click()
    time.sleep(1)
    i+=1

driver.quit()




