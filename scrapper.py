import configparser
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import requests
from PIL import Image
from io import BytesIO

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def setup_driver(driver_path):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    return driver

def scroll_and_load_images(driver, url, scroll_count, scroll_delay):
    driver.get(url)
    for _ in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_delay)
    return BeautifulSoup(driver.page_source, 'html.parser')

def extract_image_urls(soup):
    img_urls = []
    for img_tag in soup.find_all('img'):
        img_src = img_tag.get('src')
        if img_src and "http" in img_src:
            img_urls.append(img_src)
    return img_urls

def download_images(img_urls, directory_name, search_query):
    os.makedirs(directory_name, exist_ok=True)
    for i, img_url in enumerate(img_urls[:200]):
        try:
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            img.save(f"{directory_name}/{search_query.replace(' ', '')}{i + 1}.jpg")
        except Exception as e:
            print(f"Failed to download {search_query} image {i + 1}: {e}")

def main():
    config = load_config()
    search_query = input("Enter the search query (e.g., 'blonde man'): ")
    url = f"https://in.pinterest.com/search/pins/?q={search_query}"
    driver = setup_driver(config['selenium']['driver_path'])
    soup = scroll_and_load_images(driver, url, int(config['selenium']['scroll_count']), int(config['selenium']['scroll_delay']))
    img_urls = extract_image_urls(soup)
    print(f"Found {len(img_urls)} images for '{search_query}'.")
    directory_name = f"{config['directories']['download_dir']}_{search_query.replace(' ', '_')}"
    download_images(img_urls, directory_name, search_query)
    driver.quit()

if __name__ == "__main__":
    main()