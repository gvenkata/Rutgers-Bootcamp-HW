from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from splinter import Browser
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pymongo

def scrape():
    mars_news()
    mars_feature_img()
    mars_weather()
    


def mars_news():
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://mars.nasa.gov/news/'
    driver.get(url)

    html =  driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find('div', class_='list_text')

    title = articles.find('div', class_="content_title")
    desc = articles.find('div', class_="article_teaser_body")
    date = articles.find('div', class_="list_date")
    a_title=title.text
    a_desc=desc.text
    a_date=date.text

    article = {}

    article["title"] = a_title
    article["desc"] = a_desc
    article["date"] = a_date

    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_scrape
    db.marsnews.insert(article)
    print("Article Data Uploaded!")
    driver.close()

def mars_feature_img():

    executable_path = {'executable_path':'./chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    button = browser.find_by_xpath("//a[@class='button fancybox']")
    featured_image_url = "https://www.jpl.nasa.gov" + button["data-fancybox-href"]
    mars_img = {}
    mars_img["feature_img"] = featured_image_url
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_scrape
    db.marsimg.insert(mars_img)
    print("Feature Image Data Uploaded!")
    browser.quit()

def mars_weather():
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('div', class_='content')
    for result in results:
        author = result.find('strong', class_='fullname show-popup-with-id u-textTruncate')
        if author.text == "Mars Weather":
            weather = result.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
            break
    mars_weather = weather.text
    weather = {}
    weather["report"] = mars_weather
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_scrape
    db.marsweather.insert(weather)
    print("Weather Data Uploaded!")

    def mars_facts():
        executable_path = {'executable_path':'./chromedriver.exe'}
        browser = Browser('chrome', **executable_path)
        browser.visit('https://space-facts.com/mars/')
        url='https://space-facts.com/mars/'
        tables = pd.read_html(url)
        mars_earth_frame = tables[0]
        mars_earth_frame

        mars_table = mars_earth_frame[['Mars - Earth Comparison', 'Mars']]
        mars_table = mars_table.rename(columns={"Mars - Earth Comparison": "Mars Metric", "Mars": "Value"})
        mar_table_html = mars_table.to_html()

        table = {}
        table["html"] = mars_table_html
        conn = "mongodb://localhost:27017"
        client = pymongo.MongoClient(conn)
        db = client.mars_scrape
        db.marstable.insert(table)
        print("Table HTML Uploaded!")
    
