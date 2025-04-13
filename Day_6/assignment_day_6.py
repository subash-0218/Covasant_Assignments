
# Question-9:
# Given a URL, download that and parse 
# and download all links inside that page in asyncio 
# BeautifulSoup for parsing html, requests for downloading


from bs4 import BeautifulSoup
import asyncio
import aiohttp
from urllib.parse import urljoin
import time


async def download_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
    
def parse_page_links(response,base_url):
    soup = BeautifulSoup(response,"html.parser")
    links = set()
    
    for a_tag in soup.find_all("a", href=True):
        link = urljoin(base_url,a_tag["href"])
        links.add(link)
            
    return links
    
    
async def download_all(url):   
    html = await download_page(url)   
    links = parse_page_links(html,url) 
    
    print(f"Links found in {url}:\n")
    for link in links:
        print(link)
            
    tasks = [asyncio.create_task(download_page(link)) for link in links]   
    result = [await task for task in tasks]
    
    return result


if __name__ == "__main__":
    url = "https://www.google.co.in/?gws_rd=ssl"
    start_time = time.time()
    asyncio.run(download_all(url))
    print("\n---Successfully downloaded the total content from given url ---")
    print(f"\nTotal Time taken : {time.time() - start_time} seconds")


#---Successfully downloaded the total content from given url ---
#Total Time taken : 1.4462833404541016 second
