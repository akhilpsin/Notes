from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


lines=[['Profile URL','Name','Price','BHKS','WhyBuy','Amenities','Swimming Pool','Gymnasium','Status','Price per Sqft','Launch Date','Possession by',
        'Total Towers','Total Units','Project Type','Property Type','Project Area','Occupancy Certificate','Commencement Certificate','Full Address',
        'Pincode','About Developer','Specifications','Place','1 BHK','2 BHK','3 BHK','4 BHK','5 BHK','BHK Above 5']]

line1=[]
#-Input excel file with all the address address under "SOURCE_ADDRESS" coulmn-
df = pd.read_excel('input.xlsx') # can also index sheet by name or fetch all sheets
add = df['SOURCE_ADDRESS'].tolist()
add = [x for x in add if str(x) != 'nan']# removes all empty list elements

m=1
for i in add:
    #----------------------Link ----------------------------
    url=i
    print(str(m)+')'+str(url))
    m=m+1

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
        #print(bhks)
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

    #print(amenities)

    if 'swimming' in amenities.lower():
        Swimming_Pool='Yes'
    else:
        Swimming_Pool='Detail not provided'
    if 'gymnasium' in amenities.lower():
        Gymnasium='Yes'
    else:
        Gymnasium='Detail not provided'
    


    try:
        all_det = (soup.find("div", {"class":"proj-info__data"}).text).strip()
        dll_de_list=all_det.split('\n')
    
        while("" in dll_de_list) :
            dll_de_list.remove("")
    except:
        dll_de_list='data not available in site'

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


    #print(Full_Address)
    splits=Full_Address.split(',')
    if len(splits)==1:
        Place=splits[0]
    elif len(splits)==2:
        Place=splits[0]
    elif len(splits)==3:
        Place=splits[-2]
    elif len(splits)==4:
        Place=splits[-2]
    else:
        Place=splits[-3]

    if '1' in bhks:
        bhk1='yes'
    else:
        bhk1='No'
        
    if '2' in bhks:
        bhk2='yes'
    else:
        bhk2='No'
        
    if '3' in bhks:
        bhk3='yes'
    else:
        bhk3='No'
        
    if '4' in bhks:
        bhk4='yes'
    else:
        bhk4='No'
        
    if '5' in bhks:
        bhk5='yes'
    else:
        bhk5='No'

    if '6' in bhks:
        bhk6='yes'
    else:
        bhk6='No'
        
    #print("---------------------------------------------------------------")

 
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
    items=[i,name,price,bhks,whyBuy,amenities,Swimming_Pool,Gymnasium,Status,Price_per_Sqft,Launch_Date,Possession_by,Total_Towers,Total_Units,Project_Type,
           Property_Type,Project_Area,Occupancy_Certificate,Commencement_Certificate,Full_Address,Pincode,about_developer,Specifications,Place,bhk1,bhk2,
           bhk3,bhk4,bhk5,bhk6]

    for p in range(28):
        items[p]=(items[p].encode("ascii", "ignore")).decode()
       
        
    lines.append(items)
    
                
df=pd.DataFrame(lines)
df.to_csv('MagicBrickFullData2k.csv', index=False,encoding='utf-8')

print("Sucessfully generated output CSV")

    


   
    
    


    
        
