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

#-------------------------------Code Start here-------------------------------
links=[]
titles=[]
bodys=[]

#-Input excel file with all the address address under "SOURCE_ADDRESS" coulmn-
df = pd.read_excel('input.xlsx') # can also index sheet by name or fetch all sheets
links = df['SOURCE_ADDRESS'].tolist()
links = [x for x in links if str(x) != 'nan']

m=0
for link in links:
    body=browser.get(link)
    time.sleep(30) #---------------------5 second sleep as requested
    
    title_elem = browser.title#-----------------------Title name
    #print(title_elem)
    titles.append(title_elem)
    
    body_elem = browser.find_element_by_xpath("//body")
    source_body=body_elem.get_attribute('outerHTML')
    source_body = BeautifulSoup(source_body, 'html.parser')
    body_text=source_body.text #------------------body text

    replace='''About cookies on this siteWe use cookies to collect and analyse information on site performance and usage, to provide social media features and to enhance and customise content and advertisements.Learn moreAllow all cookiesCookie settingsAbout cookies on this siteCookie settingsCookie declarationCookies used on the site are categorized and below you can read about each category and allow or deny some or all of them. When categories than have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally you can see a list of cookies assigned to each category and detailed information in the cookie declaration.Learn moreAllow all cookiesDeny allNecessary cookiesSome cookies are required to provide core functionality. The website won't function properly without these cookies and they are enabled by default and cannot be disabled.PreferencesPreference cookies enables the web site to remember information to customize how the web site looks or behaves for each user. This may include storing selected currency, region, language or color theme.Analytical cookiesAnalytical cookies help us improve our website by collecting and reporting information on its usage.Marketing cookiesMarketing cookies are used to track visitors across websites to allow publishers to display relevant and engaging advertisements.Other cookiesThe cookies in this category have not yet been categorized and the purpose may be unknown at this time.Cookies used on the site are categorized and below you can read about each category and allow or deny some or all of them. When categories than have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally you can see a list of cookies assigned to each category and detailed information in the cookie declaration.Learn moreNecessary cookiesSome cookies are required to provide core functionality. The website won't function properly without these cookies and they are enabled by default and cannot be disabled.NameHostnamePathExpiryTagscookiehubwww.energy-storage.news/365 daysUsed by CookieHub to store information about whether visitors have given or declined the use of cookie categories used on the site.PreferencesPreference cookies enables the web site to remember information to customize how the web site looks or behaves for each user. This may include storing selected currency, region, language or color theme.NameHostnamePathExpiryTagsCONSENT.youtube.com/5987 days, 9 hours3rd partyUsed by Google to store user consent preferencesVISITOR_INFO1_LIVE.youtube.com/180 days3rd partyA cookie that YouTube sets that measures your bandwidth to determine whether you get the new player interface or the old.Analytical cookiesAnalytical cookies help us improve our website by collecting and reporting information on its usage.NameHostnamePathExpiryTags_ga.energy-storage.news/730 daysContains a unique identifier used by Google Analytics to determine that two distinct hits belong to the same user across browsing sessions._gid.energy-storage.news/1 dayContains a unique identifier used by Google Analytics to determine that two distinct hits belong to the same user across browsing sessions._gat_*.energy-storage.news/1 hourUsed by Google Analytics to throttle request rate (limit the collection of data on high traffic sites)_ga.anchor.fm/730 days3rd partyContains a unique identifier used by Google Analytics to determine that two distinct hits belong to the same user across browsing sessions._gid.anchor.fm/1 day3rd partyContains a unique identifier used by Google Analytics to determine that two distinct hits belong to the same user across browsing sessions._gat.anchor.fm/1 hour3rd partyUsed by Google Analytics to throttle request rate (limit the collection of data on high traffic sites)YSC.youtube.com/Session3rd partyThis cookie is set by YouTube video service on pages with YouTube embedded videos to track views.Marketing cookiesMarketing cookies are used to track visitors across websites to allow publishers to display relevant and engaging advertisements.NameHostnamePathExpiryTags__gads.energy-storage.news/390 daysGoogle advertising cookie set on the website's domain (unlike the other Google advertising cookies that are set on doubleclick.net domain). According to Google the cookie "serves purposes such as measuring interactions with the ads on that domain and preventing the same ads from being shown to you too many times".IDE.doubleclick.net/390 days3rd partyUsed by Google's DoubleClick to serve targeted advertisements that are relevant to users across the web. Targeted advertisements may be displayed to users based on previous visits to a website. These cookies measure the conversion rate of ads presented to the user.Other cookiesThe cookies in this category have not yet been categorized and the purpose may be unknown at this time.NameHostnamePathExpiryTagsvisitor_id83602.pardot.com/3650 days3rd partyvisitor_id83602-hash.pardot.com/3650 days3rd partylpv83602pi.pardot.com/1 hour3rd partyvisitor_id83602www.energy-storage.news/3650 daysvisitor_id83602-hashwww.energy-storage.news/3650 daysreduxPersist%3Acomplianceanchor.fm/7 days3rd partyreduxPersist%3AlocalStorageanchor.fm/7 days3rd partyreduxPersistIndexanchor.fm/7 days3rd partySave settingsCookie settings'''

    body_text=body_text.replace(replace,'')
    body_text=body_text.split('Email Address Next')[0]
    body_text=body_text.split('© Copyright')[0]
    
    body_text=body_text.replace('\n','')
    body_text=body_text.replace(',','')
    #print(body_text)
    #print("----------------------------------------------------------------------------------------------------")
    bodys.append(str(body_text))
    m=m+1
    print(m)
            
percentile_list = pd.DataFrame(
    {'URL': links,
     'Body Text': bodys,
     'Title': titles,
    })

percentile_list.to_csv('out.csv', index=False)

print("Sucessfully generated output CSV")


