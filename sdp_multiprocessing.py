import requests
import multiprocessing
import re
import validators

from bs4 import BeautifulSoup

import time

from Models.Article.article import Article
from Models.Feed.feed import Feed

base_url = "https://www.sdpnoticias.com"

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_all_sites(urls):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(parse_feeds, urls)

def get_urls():
    page = requests.get(base_url) 
    soup = BeautifulSoup(page.content, 'html.parser')
    #Find main menu that contains all the sections of articles
    news_menu = soup.find("div", "HamburgerMenu")
    #Fetch tags and its urls
    tags = [e.string for e in news_menu.find_all("a")]
    urls = [base_url + e["href"] for e in news_menu.find_all("a", href=True) if not re.match(r"http.+",e["href"])]
    return urls

# parse_page_feeds parses each article inside the section page, then it gathers its article to complete the task
def parse_feeds(url):
    with session.get(url) as response :
        bs = BeautifulSoup(response.content, "html.parser")
        articles = [e for e in bs.find_all("article", "articleModule")]
        for e in articles:
            feed = get_attributes_feed(e)
            if feed != None:
                article= parse_page_articles(feed.get_url())

#parse_page_articles receives a feed's URL and returns an article
def parse_page_articles(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        bs = BeautifulSoup(page.content, "html.parser")
        article = get_attributes_article(bs)
        return article

"""
get_attributes_feed gathers all the attributes of one feed, 
there are some conditions to be a valid feed. It must contain : 
* Valid URL
* Title
"""
def get_attributes_feed(feed):
    title_reg_exp = r'title'
    date_reg_exp = r'date'
    img_reg_exp = r'lazy'
    link_reg_exp = r"(page-link|link-container)"
    content = ""

    if feed.find(class_=re.compile(title_reg_exp)) == None:
        return
    title = feed.find(class_=re.compile(title_reg_exp)).text
    title = " ".join(title.split())

    url = feed.find('a', re.compile(link_reg_exp) ,href=True)["href"]
    url = base_url + url
    print("URL ---> ", url)
    if not validators.url(url):
        return None 
    
    img = feed.find('img', re.compile(img_reg_exp))
    if img == None:
        img = ""
    else:
        img = img["src"]
    date = feed.find('div', re.compile(date_reg_exp))
    if date == None:
        date = "00:00"
    else:
        print(date.attrs)
        date = date.text.rstrip("\n")
  
    new_feed = Feed(title,img,content,date,url)
    print(new_feed)
    return new_feed

"""
get_attributes_article gathers a whole article from a feed
There are some custom tag in some articles
Example :
tag : h2 with class : h1
"""
def get_attributes_article(article):
    reg_title = r"SDPArticle__title"
    title = article.find("h1",re.compile(reg_title))
    
    reg_div_content = r"SDPArticle__content"
    div_content=article.find("div", re.compile(reg_div_content))
    
    reg_subtitle = r"SDPArticle__epigraph"
    if div_content.find("h3", re.compile(reg_subtitle)):
        subtitle = div_content.find("h3", re.compile(reg_subtitle)).text.rstrip("\n")
    else:
        subtitle = None
    
    reg_content = r"SDPArticle__body"
    content = div_content.find("div", re.compile(reg_content)).text

    reg_article_info = r"SDPArticle__info"
    reg_date = r"article-date"
    reg_time = reg_date
    time_container = article.find("div", re.compile(reg_article_info))
    date = time_container.find("time", re.compile(reg_date))
    date = date.attrs["datetime"]
    time = time_container.find("time", re.compile(reg_time))
    time = time.attrs["datetime"]
  
    reg_author = r"article-author"
    author = div_content.find("span", re.compile(reg_author))
    
    reg_media = r"SDPArticle__media"
    if article.find("div", re.compile(reg_media)):
        classes_img = "i-amphtml-fill-content i-amphtml-replaced-content"
        div_media = article.find("div", re.compile(reg_media))
        figure = div_media.find("amp-img")
        image = figure["src"]
    else:
        image = None
    new_article =  Article(title.text.rstrip("\n"), subtitle, image, content, author, date, time)
    print(new_article)
    return new_article

if __name__ == "__main__":
    start_time = time.time()
    download_all_sites(get_urls())
    duration = time.time() - start_time
    print(f"Downloaded  {duration} seconds")