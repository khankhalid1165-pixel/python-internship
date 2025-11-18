import requests
from bs4 import BeautifulSoup
import time

class NewsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def scrape_bbc_news(self):
        """Scrape headlines from BBC News"""
        try:
            url = "https://www.bbc.com/news"
            response = self.session.get(url)
            response.raise_for_status()  # Raise exception for bad status codes
            
            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = []
            
            # Look for headline elements - BBC uses specific classes for headlines
            headline_elements = soup.find_all(['h2', 'h3'], class_=lambda x: x and any(cls in str(x) for cls in ['sc-4fedabc7-3', 'gs-c-promo-heading']))
            
            # Alternative approach if specific classes don't work
            if not headline_elements:
                headline_elements = soup.find_all(['h2', 'h3'])[:20]  # Limit to first 20
            
            for headline in headline_elements:
                title = headline.get_text().strip()
                if title and len(title) > 10:  # Filter out very short text
                    headlines.append(title)
            
            return headlines[:15]  # Return top 15 headlines
            
        except requests.RequestException as e:
            print(f"Error fetching BBC News: {e}")
            return []
    
    def scrape_reuters_news(self):
        """Scrape headlines from Reuters"""
        try:
            url = "https://www.reuters.com/"
            response = self.session.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = []
            
            # Reuters headline selectors
            headline_elements = soup.find_all(['h2', 'h3', 'h4'], 
                                            class_=lambda x: x and any(cls in str(x).lower() for cls in ['heading', 'title', 'headline']))
            
            for headline in headline_elements:
                title = headline.get_text().strip()
                if title and len(title) > 10:
                    headlines.append(title)
            
            return headlines[:15]
            
        except requests.RequestException as e:
            print(f"Error fetching Reuters: {e}")
            return []
    
    def save_headlines_to_file(self, headlines, filename="news_headlines.txt"):
        """Save headlines to a text file"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("TOP NEWS HEADLINES\n")
                file.write("=" * 50 + "\n\n")
                
                for i, headline in enumerate(headlines, 1):
                    file.write(f"{i}. {headline}\n")
                
                file.write(f"\nTotal headlines scraped: {len(headlines)}")
                file.write(f"\nScraped at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            print(f"Headlines saved to {filename}")
            return True
            
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

def main():
    scraper = NewsScraper()
    
    print("Starting web scraping for news headlines...")
    
    # Scrape from multiple sources
    bbc_headlines = scraper.scrape_bbc_news()
    reuters_headlines = scraper.scrape_reuters_news()
    
    # Combine and deduplicate headlines
    all_headlines = list(set(bbc_headlines + reuters_headlines))
    
    print(f"Scraped {len(all_headlines)} unique headlines")
    
    # Save to file
    if all_headlines:
        scraper.save_headlines_to_file(all_headlines)
        
        # Display first 5 headlines
        print("\nSample Headlines:")
        for i, headline in enumerate(all_headlines[:5], 1):
            print(f"{i}. {headline}")
    else:
        print("No headlines were scraped.")

if __name__ == "__main__":
    main()