from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib

def __selGetImage(url):
        print(url)
        folder = "/tmp/"
        uri = []
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver=webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        r=driver.find_elements_by_tag_name('img')
        for v in r[:2]:
                src = v.get_attribute("src")
                uri.append(src)
                pos = len(src) - src[::-1].index('/')
                print src[pos:]
                g=urllib.urlretrieve(src, "/".join([folder, "image.png"]))
                

def getImage(query):
        query = query.replace(" ","+")
        __selGetImage("https://www.shutterstock.com/search?search_source=base_landing_page&language=en&searchterm=" + query + "+&image_type=all")
