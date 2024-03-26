from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
  browser = p.chromium.launch()
  page = browser.new_page()
  page.goto("https://news.yahoo.com/") 

  news_data=[]

  for i in range(1,20):
    title, url, desc = "","",""
    title = page.query_selector("//html//body//div[3]//div//main//div[4]//ul//li["+str(i)+"]").text_content()
    url = page.query_selector("//html//body//div[3]//div//main//div[4]//ul//li["+str(i)+"]//div[1]//div[2]//h3//a").get_attribute('href') 
    desc = page.query_selector("//html//body//div[3]//div//main//div[4]//ul//li["+str(i)+"]//div[1]//div[2]//p").text_content()

    news_data.append([i,title,desc,"https://news.yahoo.com"+url])

  browser.close()

  with open('yahoo_news_V1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank', 'Title', 'Description', 'News link'])
    writer.writerows(news_data)
