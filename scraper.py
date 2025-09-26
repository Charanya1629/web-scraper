import requests
from bs4 import BeautifulSoup
import os

# 1. Define the URL of the news website to scrape
# NOTE: Replace this with your chosen news site's URL
URL = 'http://quotes.toscrape.com/' # Using a safe, public scraping sandbox for the example

# 2. Define the output file name
OUTPUT_FILE = 'headlines.txt'

def scrape_headlines(url, output_file):
    """
    Fetches, parses, and saves news headlines from a given URL to a text file.
    """
    print(f"Starting web scraping on: {url}")
    print("---------------------------------------")

    try:
        # Step 1: Use requests to fetch the HTML content [cite: 8, 13]
        # Adding a User-Agent is good practice (a response to Interview Q3)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        
        # Check for successful HTTP status code [cite: 22]
        response.raise_for_status() # Raises an HTTPError for 4xx or 5xx status codes
        
    except requests.exceptions.RequestException as e:
        # Step 9 (try-except block) for handling network errors [cite: 21]
        print(f"Error fetching the URL: {e}")
        return

    # Step 2: Use BeautifulSoup to parse the HTML content 
    # We use 'html.parser' for basic HTML parsing
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # In this example, we'll find the actual quote text which is in a <span> with class 'text'
    # For a real news site, you'd target tags like <h2>, <h3>, or a specific <div>/<a> tag with a unique class/id [cite: 9, 18]
    
    # We use soup.find_all() to get all matching elements [cite: 16]
    # **Targeting all 'span' tags with the class 'text' (simulating finding headlines)**
    headline_tags = soup.find_all('span', class_='text') 
    
    headlines = []
    if headline_tags:
        for tag in headline_tags:
            # Step 8: Use .text to extract the string content without HTML tags [cite: 20]
            headline = tag.text.strip().replace('“', '').replace('”', '') # Clean up the quote marks
            headlines.append(headline)
            print(f"- {headline}")
    else:
        print("No headlines found with the specified tag/class.")
        return

    # Step 3: Save the titles in a .txt file 
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(headline + '\n')
        
        # Confirmation message
        print("---------------------------------------")
        print(f"Successfully scraped {len(headlines)} headlines.")
        print(f"Headlines saved to: {os.path.abspath(output_file)}")
        
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    scrape_headlines(URL, OUTPUT_FILE)