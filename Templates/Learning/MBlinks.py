from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe" # ACCESSING CHROME THROUGH BINARY LOCATION
chrome_driver_path = r"C:\chromedriver_win32\chromedriver.exe" # CHROME PATH
browser = webdriver.Chrome(chrome_driver_path, options=options)


from bs4 import BeautifulSoup
import requests
import csv
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



from selenium.webdriver.common.action_chains import ActionChains



#--------------------------------------------------------------
url='https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Pune'
urls=browser.get(url)
time.sleep(100)

print('time sleep done')

time.sleep(5)

content= browser.find_element_by_xpath("//div[contains(@class,'SRListing')]")
source_body=content.get_attribute('outerHTML')
source_body = BeautifulSoup(source_body, 'html.parser')

m=1
f=open('3.txt','a')
for ele in source_body.find_all("div", {"class":"m-srp-card__desc flex__item"}):
    print(m)
    m=m+1
    try:
        link=ele.find(href=True)
        url=link['href']
    except:
        url="nill"
        
    
    
    line=str(url)+'\n'

    f.write(line)
    
f.close()  
print('Sucessfully completed')
