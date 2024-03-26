from playwright.async_api import async_playwright  
import asyncio  
  
async def scrape_data():  
    async with async_playwright() as p:  
        # Launch a headless browser  
        browser = await p.chromium.launch(headless=True)  
        page = await browser.new_page()  
          
        # Go to the webpage  
        await page.goto('YOUR_PAGE_URL')  
          
        # Select the year 2019 from the dropdown  
        await page.select_option('#selectedYear_label', '2019')  
          
        # Click the refresh button  
        await page.click('text="Refresh"')  
          
        # Wait for the data to load by checking if a specific element is present  
        await page.wait_for_selector('#vchgroupTable:0:j_idt134:0:j_idt136')  
          
        # Extract the table data  
        # This is a simplified example, replace with the actual logic needed to extract your data  
        rows = await page.query_selector_all('#vchgroupTable_data tr')  
        data = []  
        for row in rows:  
            cells = await row.query_selector_all('td[role="gridcell"]')  
            row_data = []  
            for cell in cells:  
                value = await cell.text_content()  
                row_data.append(value.strip())  
            data.append(row_data)  
          
        # Close the browser  
        await browser.close()  
          
        # Return the extracted data  
        return data  
  
# Run the function and print the results  
data = asyncio.run(scrape_data())  
for row in data:  
    print(row)  
