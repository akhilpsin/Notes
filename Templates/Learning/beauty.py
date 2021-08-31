from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


lines=[['Profile URL','Name','Price','BHKS','WhyBuy','Amenities','Status','Price per Sqft','Launch Date','Possession by','Total Towers','Total Units','Project Type',
        'Property Type','Project Area','Occupancy Certificate','Commencement Certificate','Full Address','Pincode','About Developer','Specifications']]

line1=[]
#-Input excel file with all the address address under "SOURCE_ADDRESS" coulmn-
df = pd.read_excel('input.xlsx') # can also index sheet by name or fetch all sheets
add = df['SOURCE_ADDRESS'].tolist()
add = [x for x in add if str(x) != 'nan']# removes all empty list elements


for i in add:

    #----------------------Link ----------------------------
    url=i
    print(url)

    #---------------------- Source code------------------------------------------------------
    source = requests.get(url,verify=False).text
    soup  = BeautifulSoup(source, 'html.parser')

    #----------------------Extracting data------------------------------------------------------
    try:
        name = (soup.find("h1", {"class":"heading"}).text).strip()
    except:
        name = 'data not available in site'  

    try:
        price = (soup.find("div", {"class":"proj-info__price"}).text).strip()
    except:
        price = 'data not available in site'  

    try:
        bhks = (soup.find("div", {"class":"proj-info__prop"}).text).strip()
    except:
        bhks = 'data not available in site'  

    try:
        whyBuy = soup.find("div", {"class":"prj-why-buy"}).text
        whyBuy=(whyBuy.replace('Download Brochure','')).strip()
    except:
        whyBuy='data not available in site'  

    try:
        amenities = soup.find("div", {"class":"amenities"}).text
        amenities=amenities.replace('\n','')
        amenities=amenities.replace(' 											',',')
        amenities=amenities.replace('											',',')
    except:
        amenities = 'data not available in site'  



    all_det = (soup.find("div", {"class":"proj-info__data"}).text).strip()
    dll_de_list=all_det.split('\n')
    
    while("" in dll_de_list) :
        dll_de_list.remove("")

    if 'Status' in dll_de_list:
        Status=dll_de_list[dll_de_list.index('Status')+1]
    else:
        Status='data not available in site'       
    if 'Price per Sqft' in dll_de_list:
        Price_per_Sqft=dll_de_list[dll_de_list.index('Price per Sqft')+1]
    else:
        Price_per_Sqft='data not available in site'
    if 'Launch Date' in dll_de_list:
        Launch_Date=dll_de_list[dll_de_list.index('Launch Date')+1]
    else:
        Launch_Date='data not available in site'
    if 'Possession by' in dll_de_list:
        Possession_by=dll_de_list[dll_de_list.index('Possession by')+1]
    else:
        Possession_by='data not available in site'
    if 'Total Towers' in dll_de_list:
        Total_Towers=dll_de_list[dll_de_list.index('Total Towers')+1]
    else:
        Total_Towers='data not available in site'        
    if 'Total Units' in dll_de_list:
        Total_Units=dll_de_list[dll_de_list.index('Total Units')+1]
    else:
        Total_Units='data not available in site'   
    if 'Project Type' in dll_de_list:
        Project_Type=dll_de_list[dll_de_list.index('Project Type')+1]
    else:
        Project_Type='data not available in site'
        
    if 'Property Type' in dll_de_list:
        Property_Type=dll_de_list[dll_de_list.index('Property Type')+1]
    else:
        Property_Type='data not available in site'
    if 'Commencement Certificate' in dll_de_list:
        Commencement_Certificate=dll_de_list[dll_de_list.index('Commencement Certificate')+1]
    else:
        Commencement_Certificate='data not available in site'   
    if 'Full Address' in dll_de_list:
        Full_Address=dll_de_list[dll_de_list.index('Full Address')+1]
    else:
        Full_Address='data not available in site'
    if 'Pincode' in dll_de_list:
        Pincode=dll_de_list[dll_de_list.index('Pincode')+1]
    else:
        Pincode='data not available in site'
    if 'Project Area' in dll_de_list:
        Project_Area=dll_de_list[dll_de_list.index('Project Area')+1]
    else:
        Project_Area='data not available in site'
        
    if 'Occupancy Certificate' in dll_de_list:
        Occupancy_Certificate=dll_de_list[dll_de_list.index('Occupancy Certificate')+1]
    else:
        Occupancy_Certificate='data not available in site'
        
    try:
        Specifications = (soup.find("div", {"class":"other-info webkit__scroll"}).text).strip()
    except:
        Specifications = 'data not available in site'
    try:
        about_developer = (soup.find("div", {"class":"about-developer__builder"}).text).strip()
    except:
        about_developer = 'data not available in site'

 
    #print(name)
    #print(price.strip())
    #print('bhks: ',bhks)
    #print(whyBuy)
    #print(amenities)
    #print('Status=',Status)
    #print('Price_per_Sqft=',Price_per_Sqft)
    #print('Launch_Date=',Launch_Date)
    #print('Possession_by=',Possession_by)
    #print('Total_Towers=',Total_Towers)
    #print('Total_Units=',Total_Units)
    #print('Project_Type=',Project_Type)
    #print('Property_Type=',Property_Type)
    #print('Commencement_Certificate=',Commencement_Certificate)
    #print('Full_Address=',Full_Address)
    #print('Pincode=',Pincode)
    #print('Project_Area=',Project_Area)
    #print('Occupancy_Certificate=',Occupancy_Certificate)
    #print('******************')
    #print('dll_de_list=',dll_de_list)
    #print('Specifications: ',Specifications)
    #print('about_developer: ',about_developer)
    
    #print('--------------------------------------------------------')
    items=[i,name,price,bhks,whyBuy,amenities,Status,Price_per_Sqft,Launch_Date,Possession_by,Total_Towers,Total_Units,Project_Type,Property_Type,Project_Area,Occupancy_Certificate,
           Commencement_Certificate,Full_Address,Pincode,about_developer,Specifications]

    for p in range(21):
        items[p]=(items[p].encode("ascii", "ignore")).decode()
       
        
    lines.append(items)
    
                
df=pd.DataFrame(lines)
df.to_csv('MagicBrickSampleData.csv', index=False,encoding='utf-8')

print("Sucessfully generated output CSV")

    


   
    
    


    
        
