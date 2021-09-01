from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" # ACCESSING CHROME THROUGH BINARY LOCATION
chrome_driver_path = r"C:\Users\akhil\Desktop\Clone\chromedriver_win32\chromedriver.exe" # CHROME PATH
browser = webdriver.Chrome(chrome_driver_path, options=options)


from bs4 import BeautifulSoup
import requests
import csv
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#--------------------------------------------------------------
url='https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Pune'
urls=browser.get(url)
time.sleep(70)
print('start in 30 sec')
time.sleep(40)

content= browser.find_element_by_xpath("//div[contains(@class,'SRListing')]")

source_body=content.get_attribute('outerHTML')
source_body = BeautifulSoup(source_body, 'html.parser')

m=1
f=open('MBsampleLinks.txt','a')
for ele in source_body.find_all("div", {"class":"m-srp-card__desc flex__item"}):
    print(m)
    m=m+1
    try:
        link=ele.find(href=True)
        url=link['href']
        title=(link.text).strip()
    except:
        title="nill"
        url="nill"
        
    
    
    line=str(title)+'\t'+str(url)+'\n'
    
    print(str(title)+'\n'+str(url))
    f.write(line)
    
f.close()  
print('Sucessfully completed')
