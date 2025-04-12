
# Question-9:
# Given a URL, download that and parse 
# and download all links inside that page in asyncio 
# BeautifulSoup for parsing html, requests for downloading


from bs4 import BeautifulSoup
import asyncio
import aiohttp
from urllib.parse import urljoin


async def download_page(session,url):
    
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
    
    async with aiohttp.ClientSession() as session:
        
        html = await download_page(session,url)
        
        links = parse_page_links(html,url)
        
        print(f"Links found in {url}:\n")
        for link in links:
            print(link)
            
        tasks = [download_page(session,link) for link in links]
        
        await asyncio.gather(*tasks)
        
        
if __name__ == "__main__":
    url = "https://www.google.co.in/?gws_rd=ssl"
    asyncio.run(download_all(url))
