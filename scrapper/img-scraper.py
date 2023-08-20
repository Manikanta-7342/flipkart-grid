import requests
import os
import json

def getImages():
    # Create the 'data' folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Load image links from links.json
    with open('links.json', 'r') as links_file:
        image_links = json.load(links_file)

    # Download images and save them in the 'data' folder
    for index, image_link in enumerate(image_links, start=1):
        try:
            image_link = image_link[:-5]
            response = requests.get(image_link)
            if response.status_code == 200:
                image_extension = image_link.split('.')[-1]
                image_filename = f'data/image_{index}.{image_extension}'
                with open(image_filename, 'wb') as image_file:
                    image_file.write(response.content)
                print(f"Image {index} downloaded: {image_filename}")
            else:
                print(f"Failed to download image {index}")
        except Exception as e:
            print(f"Error downloading image {index}: {str(e)}")
