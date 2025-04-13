
# Question-8:
# Given a URL, download that and parse 
# and download all links inside that page 
# Use ThreadPoolExecutor or ProcessPoolExecutor 
# BeautifulSoup for parsing html, requests for downloading
    
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import time

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
    
def download_all_threading(url,workers):
    start_time = time.time()
    html = download_page(url)
    links = parse_page_links(html,url)
    
    # print(f"Links found in {url}:\n")
    # for link in links:
        # print(link)
        
    with ThreadPoolExecutor(max_workers = workers) as executor:
        list(executor.map(download_page ,links))
            
    end_time = time.time()
    total_time = round(end_time - start_time,3)
    
    return total_time
    
def download_all_sequential(url):
    start_time = time.time()
    html = download_page(url)
    links = parse_page_links(html,url)
     
    for link in links:
        download_page(link)
            
    end_time = time.time()
    total_time = round(end_time - start_time,3)
    
    return total_time


if __name__ == "__main__":   
    url = "https://www.google.co.in/?gws_rd=ssl"
    print("\n ---- Without Threading ----")
    print(f"\n Time Taken for downloading without Threading :{download_all_sequential(url)} seconds")
    print("\n ---- With Threading ----")
    print(f"\n Time Taken for downloading with Threading : {download_all_threading(url,10)} seconds")


#---- Without Threading ----
#Time Taken for downloading without Threading :13.31 seconds
#---- With Threading ----
#Time Taken for downloading with Threading : 2.659 seconds
