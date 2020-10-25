from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time

def init_browser():
    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    executable_path = {'executable_path': '/Users/kcyou/Documents/DataBootcamp/ChromeDriver/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}
    num = 5

    
    # NASA Latest Mars News
    print('Finding latest NASA Mars news.....\n')
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(num)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('div', class_='list_text')

    # print(len(articles))

    news_title = articles[0].find('a').text
    print(f'Latest News: {news_title}')

    news_p = articles[0].find('div', class_='article_teaser_body').text
    print(f'Latest Teaser: {news_p}\n')

    mars_data['latest_news'] = news_title
    mars_data['latest_teaser'] = news_p

    print(f'Current Mars Data Dict is: {mars_data}\n\n')

    # JPL Mars Space Images - Featured Image
    print('Finding featured NASA JPL Mars space image.....\n')

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(num)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find_all('article', class_='carousel_item')

    # print(len(image))

    s_url = 'https://www.jpl.nasa.gov'
    e_url = image[0].find('a', class_='button fancybox')['data-fancybox-href']
    print(f'Partial image url: {e_url}')

    featured_image_url = s_url + e_url
    print(f'Complete image url: {featured_image_url}\n')

    mars_data['featured_image_url'] = featured_image_url

    print(f'Current Mars Data Dict is: {mars_data}\n\n')


    # Mars Facts
    print('Finding Mars facts.....\n')

    url = 'https://space-facts.com/mars/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    table_info = soup.find('table', class_='tablepress tablepress-id-p-mars')

    for info in table_info.find_all('tr'):
        data = info.find('td', class_="column-1").text
        name = data.replace(':', '').rstrip()
        print(f'Name is: {name}')
    
    
    
    browser.quit()


scrape()


