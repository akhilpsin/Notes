import asyncio  
from pyppeteer import launch  
import csv  
  
async def scrape_news(base_url, csv_file_name):  
    # Launch the browser  
    browser = await launch()  
    page = await browser.newPage()  
  
    # Go to the Yahoo News homepage  
    await page.goto(base_url, waitUntil='networkidle0')  
  
    # Extract the data  
    news_data = await page.evaluate('''() => {  
        const articles = document.querySelectorAll('li.stream-item');  
        const newsData = [];  
  
        articles.forEach((article, rank) => {  
            const titleElement = article.querySelector('h3');  
            const descriptionElement = article.querySelector('p');  
            const linkElement = article.querySelector('a');  
              
            if (titleElement && linkElement && !article.className.includes('adfeedback')) {  
                const title = titleElement.innerText;  
                const description = descriptionElement ? descriptionElement.innerText : '';  
                const link = linkElement.href.startsWith('http') ? linkElement.href : base_url + linkElement.getAttribute('href');  
                  
                newsData.push({  
                    Rank: rank + 1,  
                    Title: title,  
                    Description: description,  
                    NewsLink: link  
                });  
            }  
        });  
  
        return newsData;  
    }''')  
  
    # Write the news data to a CSV file  
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:  
        writer = csv.DictWriter(file, fieldnames=['Rank', 'Title', 'Description', 'NewsLink'])  
        writer.writeheader()  
        writer.writerows(news_data)  
  
    # Close the browser  
    await browser.close()  
  
    return f'Scraped data has been written to {csv_file_name}'  
  
# Base URL of Yahoo News homepage  
base_url = "https://news.yahoo.com/"  
  
# Define the CSV file name  
csv_file_name = 'yahoo_news_articles.csv'  
  
# Run the async function  
result = asyncio.get_event_loop().run_until_complete(scrape_news(base_url, csv_file_name))  
print(result)  
