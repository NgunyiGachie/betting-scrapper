from scraper.scraper import scrape_website, save_data_to_file

url = 'https://www.ke.sportpesa.com/en/casino/aviator'

title, links, image_urls, tag_counts, valid_links = scrape_website(url)

print(f"Title: {title}\n")
print("Links on the page:")
for link in links:
    print(link)
print("\nImage URLs:")
for img_url in image_urls:
    print(img_url)
print("\nTag counts:")
for tag, count in tag_counts.items():
    print(f"{tag}: {count}")
print("\nValid links:")
for link in valid_links:
    print(link)

save_data_to_file(title, links, tag_counts.keys())