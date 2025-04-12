# Question-8:
# Given a URL, download that and parse 
# and download all links inside that page 
# Use ThreadPoolExecutor or ProcessPoolExecutor 
# BeautifulSoup for parsing html, requests for downloading
    
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

def download_page(url):
    
    response = requests.get(url)
    
    return response
    
def parse_page_links(response,base_url):
    
    soup = BeautifulSoup(response.text,"html.parser")
    
    links = set()
    
    for a_tag in soup.find_all("a", href=True):
        link = urljoin(base_url,a_tag["href"])
        links.add(link)
        
    return links
    
def download_all(url):
    
    html = download_page(url)
    
    links = parse_page_links(html,url)
    
    print(f"Links found in {url}:\n")
    for link in links:
        print(link)
    
    with ThreadPoolExecutor(max_workers = 5) as executor:
        executor.map(download_page ,links)

        
    
if __name__ == "__main__":   
    url = "https://www.google.co.in/?gws_rd=ssl"
    download_all(url)
