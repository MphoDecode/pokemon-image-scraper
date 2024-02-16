#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import cv2
import os
import pandas as pd

# Function to scrape images from the URL
def scrape_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = []
    for img in soup.find_all('img', class_='img-fixed icon-pkmn'):
        images.append(img['data-src'])
    return images

# Function to resize images and add Pokemon names
def resize_and_add_name(images):
    pokemon_names = []
    for idx, img_url in enumerate(images):
        # Download image
        img_data = requests.get(img_url).content
        with open(f"pokemon_{idx}.jpg", 'wb') as handler:
            handler.write(img_data)
        
        # Read and resize image
        img = cv2.imread(f"pokemon_{idx}.jpg")
        img_resized = cv2.resize(img, (300, 300))
        
        # Add Pokemon name to the image
        pokemon_name = img_url.split('/')[-1].split('.')[0]
        pokemon_names.append(pokemon_name)
        cv2.putText(img_resized, pokemon_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Save resized image
        cv2.imwrite(f"pokemon_resized_{idx}.jpg", img_resized)
        
        # Remove original downloaded image
        os.remove(f"pokemon_{idx}.jpg")
    
    return pokemon_names

# Main function
def main():
    url = "https://pokemondb.net/pokedex/national"
    images = scrape_images(url)
    pokemon_names = resize_and_add_name(images)
    
    # Save results to Excel file
    df = pd.DataFrame({'Pokemon Name': pokemon_names})
    df.to_excel(r"C:\Users\Mpho\OneDrive - University of Witwatersrand\Documents\pokemon images.xlsx", index=False)
    print("Images and names saved successfully.")

if __name__ == "__main__":
    main()

