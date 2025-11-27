import sys
import requests
from bs4 import BeautifulSoup
from typing import List

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def download_url_and_get_all_hrefs(url: str) -> List[str]:
    hrefs = []
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            print(f"UPOZORNĚNÍ: Stránka {url} vrátila kód {response.status_code}. Odkazy nebudou parsovány.")
            return hrefs

    except requests.exceptions.RequestException as e:
        print(f"CHYBA PŘI STAŽENÍ: {e}")
        return hrefs 

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for a_tag in soup.find_all('a'):
            href = a_tag.get('href')
            
            if href:
                hrefs.append(href)
                
    except Exception as e:
        print(f"CHYBA PŘI PARSOVÁNÍ OBSAHU: {e}")
        
    return hrefs


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("POUŽITÍ: python sixth.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1]
    
    try:
        print(f"Spouštím stahování a analýzu odkazů z: {url}")
        
        links = download_url_and_get_all_hrefs(url)
        
        if links:
            print(f"\n--- Nalezeno {len(links)} odkazů ---")
            for i, link in enumerate(links[:10]):
                print(f"[{i+1}] {link}")
            if len(links) > 10:
                print("...")
        elif links is not None:
             print("Nebyly nalezeny žádné odkazy.")

    except Exception as e:
        print(f"Program skoncil neočekávanou chybou: {e}")