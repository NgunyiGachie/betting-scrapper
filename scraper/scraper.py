import requests
from bs4 import BeautifulSoup
import re

def scrape_website(url):
    """Scrapes website and returns various data."""
    url = 'https://www.ke.sportpesa.com/en/casino/aviator'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.text
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    image_urls = [img.get('src') for img in soup.find_all('img') if img.get('src')]

    tag_counts = {}
    for tag in soup.find_all():
        tag_name = tag.name
        if tag_name:
            tag_counts[tag_name] = tag_counts.get(tag_name, 0) + 1

    valid_links = [link for link in links if re.match(r'^https?://', link)]
    return title, links, image_urls, tag_counts, valid_links

def save_data_to_file(title, links, paragraphs, filename='webpage_data.txt'):
    """Saves the scraped data to a text file."""
    with open(filename, 'w') as file:
        file.write(f"Title: {title}\n\n")
        file.write("Links on the page:\n")
        for link in links:
            file.write(f"{link}\n")
        file.write("\nText from paragraphs:\n")
        for paragraph in paragraphs:
            file.write(f"{paragraph}\n")

    print(f"\nData saved to '{filename}'")