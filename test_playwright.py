import asyncio  
from playwright.async_api import async_playwright  
import csv  
  
async def scrape_yahoo_news():  
    # Launch the browser in headless mode  
    async with async_playwright() as p:  
        browser = await p.chromium.launch()  
        page = await browser.new_page()  
  
        # Navigate to the Yahoo News homepage  
        await page.goto('https://news.yahoo.com/')  
  
        # Extract the news articles  
        articles = await page.query_selector_all('a:has(h3)')  
          
        # Prepare the list to store article data  
        news_data = []  
  
        # Iterate over the extracted articles and collect the relevant data  
        for rank, article in enumerate(articles, start=1):  
            title_element = await article.query_selector('h3')  
            title = await title_element.inner_text() if title_element else 'No Title'  
            description_element = await article.query_selector('p')  
            description = await description_element.inner_text() if description_element else 'No Description'  
            link = await article.get_attribute('href')  
  
            # Append the data to the list  
            news_data.append([rank, title, description, link])  
  
        # Close the browser  
        await browser.close()  
  
        # Write to CSV file  
        with open('yahoo_news.csv', 'w', newline='', encoding='utf-8') as file:  
            writer = csv.writer(file)  
            # Write the headers  
            writer.writerow(['Rank', 'Title', 'Description', 'News link'])  
            # Write the news data  
            writer.writerows(news_data)  
  
# Run the async function  
asyncio.run(scrape_yahoo_news())  
