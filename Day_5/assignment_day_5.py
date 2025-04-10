# Question-8:
# Given a URL, download that and parse 
# and download all links inside that page 
# Use ThreadPoolExecutor or ProcessPoolExecutor 
# BeautifulSoup for parsing html, requests for downloading
    
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def download_page(url): 
    response = requests.get(url)
    return response
    
def parse_page_links(response):
    soup = BeautifulSoup(response.text,"html.parser")
    links = set()
    
    for a_tag in soup.find_all("a", href=True):
        link = a_tag["href"]
        if link.startswith("http"):
            links.add(link)
            
    return links
    
def download_all(url):
    current_url = [url]
    with ThreadPoolExecutor(max_workers = 5) as executor:
        while current_url:
            results = list(executor.map(download_page , current_url))
            current_url = []
            for html in results:
                if html :
                    links = parse_download_links(html)
                    print("Extracted Links:",links)
                    current_url.extend(links)
        
    
if __name__ == "__main__":
  
    url = "https://www.google.co.in/?gws_rd=ssl"
    download_all(url)
