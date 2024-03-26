from playwright.async_api import async_playwright  
import csv  
import asyncio  
  
async def scrape_yahoo_news():  
    async with async_playwright() as p:  
        browser = await p.chromium.launch()  
        page = await browser.new_page()  
        await page.goto("https://news.yahoo.com/")  
          
        # Select all news items at once  
        news_items = await page.query_selector_all('selector-for-news-items')  
          
        news_data = []  
  
        for i, item in enumerate(news_items, start=1):  
            title_element = await item.query_selector('selector-for-title')  
            title = await title_element.text_content() if title_element else ""  
              
            url_element = await item.query_selector('selector-for-url')  
            url = await url_element.get_attribute('href') if url_element else ""  
              
            desc_element = await item.query_selector('selector-for-description')  
            desc = await desc_element.text_content() if desc_element else ""  
              
            news_data.append({  
                'Rank': i,  
                'Title': title,  
                'Description': desc,  
                'News link': f"https://news.yahoo.com{url}"  
            })  
  
        await browser.close()  
          
        # Write to CSV  
        with open('yahoo_news_V1.csv', 'w', newline='', '') as file:  
            fieldnames = ['Rank', 'Title', 'Description', 'News link']  
            writer = csv.DictWriter(file, fieldnames=fieldnames)  
            writer.writeheader()  
            writer.writerows(news_data)  
  
# Run the scraper  
asyncio.run(scrape_yahoo_news())  
