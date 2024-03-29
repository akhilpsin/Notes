import requests
from bs4 import BeautifulSoup
import csv

url = 'https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml'
  
headers = {  
    'Accept': 'application/xml, text/xml, */*; q=0.01',  
    'Accept-Encoding': 'gzip, deflate, br, zstd',  
    'Accept-Language': 'en-US,en;q=0.9',  
    'Connection': 'keep-alive',  
    'Content-Length': '4078',  
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',  
    'Cookie': 'primefaces.download=true; JSESSIONID=F41D140286CB6272826F6F2D9DDF3519; SERVERID_8075=vahan_ser_142_129; SERVERID=vahan_ser_152_129',  
    'Faces-Request': 'partial/ajax',  
    'Host': 'vahan.parivahan.gov.in',  
    'Origin': 'https://vahan.parivahan.gov.in',  
    'Referer': 'https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml',  
    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',  
    'Sec-Ch-Ua-Mobile': '?0',  
    'Sec-Ch-Ua-Platform': '"Windows"',  
    'Sec-Fetch-Dest': 'empty',  
    'Sec-Fetch-Mode': 'cors',  
    'Sec-Fetch-Site': 'same-origin',  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',  
    'X-Requested-With': 'XMLHttpRequest'  
}  
 
payload = {  
    'javax.faces.partial.ajax': 'true',  
    'javax.faces.source': 'groupingTable',  
    'javax.faces.partial.execute': 'groupingTable',  
    'javax.faces.partial.render': 'groupingTable',  
    'groupingTable': 'groupingTable',  
    'groupingTable_pagination': 'true',  
    'groupingTable_first': '0',  
    'groupingTable_rows': '25',  
    'groupingTable_skipChildren': 'true',  
    'groupingTable_encodeFeature': 'true',  
    'masterLayout_formlogin': 'masterLayout_formlogin',  
    'j_idt29_input': 'A',  
    'j_idt39_input': '-1',  
    'selectedRto_input': '-1',  
    'yaxisVar_input': 'Maker',  
    'xaxisVar_input': 'Vehicle Category',  
    'selectedYearType_input': 'C',  
    'selectedYear_input': '2019',  
    'groupingTable:selectMonth_input': '2019',  
    'groupingTable:selectCatgType_input': 'A',  
    'groupingTable_scrollState': '0,0',
    'javax.faces.ViewState': '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',
}  


with open('vahan_parivahan_gov.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    #Headings for CSV
    writer.writerow(['S:No','Maker','2WIC (Vehicle Category)','2WN (Vehicle Category)','2WT (Vehicle Category)','3WN (Vehicle Category)','3WT (Vehicle Category)','4WIC (Vehicle Category)','HGV (Vehicle Category)','HMV (Vehicle Category)','HPV (Vehicle Category)','LGV (Vehicle Category)','LMV (Vehicle Category)','LPV (Vehicle Category)','MGV (Vehicle Category)','MMV (Vehicle Category)','MPV (Vehicle Category)','OTH (Vehicle Category)','TOTAL','Year'])

    for y in [2019, 2020 , 2021 , 2022 , 2023 , 2024]:
        payload['selectedYear_input'] = str(y)
        payload['groupingTable:selectMonth_input']= str(y)

        curent_grp=0
        while True:
            payload['groupingTable_first'] = str(curent_grp)
            response = requests.post(url, data=payload, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'lxml')
                rows = soup.find_all('tr')
                for row in rows:
                    row_data = []
                    cells = row.find_all('td')
                    for cell in cells:
                        label = cell.text
                        row_data.append(label)
                    row_data.append(y)
                    writer.writerow(row_data)
            else:  
                print(f'Request failed with status code: {response.status_code}')
            
            if len(rows)<1:
                break
            curent_grp+=25

print("Run completed.")
