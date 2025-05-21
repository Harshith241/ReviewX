from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_path = r"C:\Users\v4vij\Downloads\Harshith-Folder\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)

url = "https://www.homedepot.com/p/Samsung-Bespoke-29-cu-ft-4-Door-French-Door-Smart-Refrigerator-with-Beverage-Center-in-Stainless-Steel-Standard-Depth-RF29BB8600QL/319503107?source=shoppingads&locale=en-US&pla&utm_source=google&utm_medium=vantage&utm_campaign=50469&utm_content=52735&mtc=SHOPPING-RM-RMP-GGL-D29A-029_013_REFRIG-NA-SAMSUNG-NA-PMAX-NA-NA-MK893629001-50469-NBR-37-NA-VNT-FY25Q1Q4_Samsung_D29A_RM_AON_REF&cm_mmc=SHOPPING-RM-RMP-GGL-D29A-029_013_REFRIG-NA-SAMSUNG-NA-PMAX-NA-NA-MK893629001-50469-NBR-37-NA-VNT-FY25Q1Q4_Samsung_D29A_RM_AON_REF-22181178953--&gad_source=1&gad_campaignid=22174782234&gbraid=0AAAAAolLu9-EX1qf5RzN33lGviyD25ylc&gclid=Cj0KCQjwoZbBBhDCARIsAOqMEZUwui0Hp5N242M537tkA-KmkzdnMZQ0XfpgiKhu43-Oa0GY49yKeoEaAu4GEALw_wcB&gclsrc=aw.ds"
driver.get(url)


try:
    xpath = '//*[@id="root"]/div/div/div[5]/div/div[1]/div/div[3]/span/h1'
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    product_name = driver.find_element(By.XPATH, xpath).text
    print("Product Name:", product_name)
except Exception as e:
    print("Error finding product name:", e)

driver.quit()


