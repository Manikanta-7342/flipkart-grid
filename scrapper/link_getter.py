import requests
from bs4 import BeautifulSoup
import json
from scrapper.flipkart.img-scraper import getImages
def getRatingandReview(url):
  url = "https://www.flipkart.com" + url
  #print(url)
  response = requests.get(url)
  try:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the dress items on the page
    dress_items = soup.find_all('div', class_='gUuXy- _16VRIQ _1eJXd3')

    return soup.find('div', class_='_3LWZlK _3uSWvT').text,soup.find('span',class_='_2_R_DZ').text
  except:
    return 0,"N/A"

image_links = []
dump_data = []
titles = []
categories = ['mens+trending+dresses','womens+trending+dresses']

def provideLinks():
    for category in categories:
      # URL of the Flipkart page you want to scrape
      url = "https://www.flipkart.com/search?q=" + category + "&otracker=search&otracker1=search&marketplace=FLIPKART"
      #print(url)

      # Send an HTTP request to the URL
      response = requests.get(url)

      # Parse the HTML content using BeautifulSoup
      soup = BeautifulSoup(response.content, 'html.parser')

      # Find all the dress items on the page
      dress_items = soup.find_all('div', class_='_1xHGtK _373qXS')

      company_items = soup.find_all('div',class_='_13oc-S')

      for item in company_items:
        try:
          pid = item.find('div')['data-id']
          titles.append(pid)
        except:
          print("Error in loading")


      # Loop through each dress item and extract relevant information
      for item in dress_items:
          try:
            # Extract data-id attribute and save it as pid
            #pid = item.find('div')['data-id']

            rating,review = getRatingandReview(str(item.find('a', class_='_3bPFwb')['href']))

            company = item.find('div', class_='_2WkVRV').text

            # Extract image URL
            image_url = item.find('img', class_='_2r_T1I')['src']

            # Extract title
            title = item.find('a', class_='IRpwTa')['title']

            # Extract price
            price = item.find('div', class_='_30jeq3').text


            data = {
                  "title": title,
                  "company": company,
                  "price": price,
                  "ratings": rating,
                  "review": review
              }
            dump_data.append(data)
            image_links.append(image_url)

          except:
               print("Error extracting information for an item")

    # Save image links to links.json
    with open("links.json", "w") as links_file:
        json.dump(image_links, links_file, indent=4)

    # Save details to dump.json
    with open("dump.json", "w") as dump_file:
        json.dump(dump_data, dump_file, indent=4)

    getImages()
