from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    mars_site = 'https://redplanetscience.com/'
    browser.visit(mars_site)
    mars_html = browser.html
    mars_soup = bs(mars_html, 'html.parser')
    
    news_title = mars_soup.find('div', class_='content_title').get_text()
    news_p = mars_soup.find_all('div', class_='article_teaser_body')[0].text


    mars_image = 'https://spaceimages-mars.com/'
    browser.visit(mars_image)
    html = browser.html
    images_soup = bs(html, 'html.parser')
    
    image_path= images_soup.find_all('img', class_='headerimage fade-in')[0]['src']
    featured_image_url = mars_image + image_path 


    mars_facts = 'https://galaxyfacts-mars.com/'
    fact_tables = pd.read_html(mars_facts)
    mars_factsDF = fact_tables[1]
    mars_factsDF.columns = ["Characteristic", "Fact"]
    mars_html_table_string = mars_factsDF.to_html()
    
    
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


     
    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_fact": str(mars_html_table_string),
        "hemisphere_images":  hemisphere_image_urls
    }

    return mars_dict