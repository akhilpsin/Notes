import requests
from bs4 import BeautifulSoup
import csv

# Function to clean up text
def clean_text(text):
    replacements = {
        'â€™': "'",
        'â€œ': '"',
        'â€”': '—', 
        'â€“': '–',
        # Add more replacements if needed
    }
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)
    text = text.encode('ascii', 'ignore').decode('ascii')
    return text
  
# The target webpage URL and base URL for relative link
url = "https://news.yahoo.com/"
base_url = "https://www.yahoo.com"
  
with requests.Session() as session:
    response = session.get(url)
  
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        list_items = soup.find_all('li', class_='stream-item js-stream-content Bgc(t) Pos(r) Mb(24px)')
  
        with open('yahoo_news.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Rank', 'Title', 'Description', 'URL'])
  
            for rank, item in enumerate(list_items, start=1):
                title_tag = item.find('h3')
                description_tag = item.find('p')
                url_tag = title_tag.find('a') if title_tag else None
  
                title = clean_text(title_tag.get_text(strip=True)) if title_tag else ''
                description = clean_text(description_tag.get_text(strip=True)) if description_tag else ''
                url = url_tag['href'] if url_tag and 'href' in url_tag.attrs else ''
                url = (base_url + url) if url.startswith('/') else url
  
                writer.writerow([rank, title, description, url])
    else:  
        print(f"Failed Status code: {response.status_code}")

print("Run completed.")
