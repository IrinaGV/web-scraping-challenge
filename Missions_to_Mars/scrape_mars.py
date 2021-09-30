from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    scraped_result = {}
    news= mars_news()
    scraped_result["mars_news"] = news[0]
    scraped_result["mars_paragraph"] = news[1]
    scraped_result["mars_image"] = mars_image()
    scraped_result["mars_facts"] = mars_facts()
    scraped_result["mars_hemisphere"] = mars_h_data()
    browser.quit()
    return scraped_result


def mars_news():
    
    mars_site= "https://redplanetscience.com/"
    browser.visit(mars_site)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = mars_soup.find_all('div', class_='content_title')[0].text
    news_p = mars_soup.find_all('div', class_='article_teaser_body')[0].text
    news = [news_title, news_p]
    return news


def  mars_image():
    mars_image = "https://spaceimages-mars.com/"
    browser.visit(mars_image)
    html = browser.html
    images_soup = bs(html, 'html.parser')
    
    image_path= images_soup.find_all('img', class_='headerimage fade-in')[0]['src']
    featured_image_url = mars_image + image_path 
    print(featured_image_url)
    return featured_image_url


def  mars_facts():
    mars_facts_url = "https://galaxyfacts-mars.com/"
    fact_tables = pd.read_html(mars_fact_url)
    mars_factsDF = fact_tables[1]
    fact_tables.columns = ['Characteristics', 'Fact']
    mars_html_table_string = mars_factsDF.to_html()
    # print(mars_facts)
    return mars_html_table_string


def mars_h_data():
    mars_hemisperes = 'https://marshemispheres.com/'
    browser.visit(mars_hemisperes)
    hemispheres_html = browser.html
    hemispheres_soup = bs(hemispheres_html, 'html.parser')
    
    hemisphere_image_urls = []
    mars_hemispheres_descr = hemispheres_soup.find_all('div', class_='description')

    for i in mars_hemispheres_descr:
        title = i.find("h3").text
        hemispheres_image = i.find("a", class_="itemLink product-item")["href"]
        
        browser.visit(mars_hemisperes + hemispheres_image)
           
        image_html = browser.html
        info = bs(image_html, "html.parser")
        
        image_url = mars_hemisperes + info.find("img", class_="wide-image")["src"]
        hemisphere_image_urls.append({"title" : title, "image_url" : image_url})

        print("")
        print(title)
        print(image_url)
        print("--------------------")
    return hemisphere_image_urls 

    
if __name__ == "__main__":
    print(scrape())