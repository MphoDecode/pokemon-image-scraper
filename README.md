# pokemon-image-scraper
Pokemon Image Scraper
This Python script allows you to scrape Pokemon images from a specified URL, resize them, add Pokemon names as annotations, and save the annotated images. It also saves the Pokemon names in an Excel file.

Requirements
Python 3.x
Libraries:
requests
BeautifulSoup
OpenCV (cv2)
pandas
Installation
This Python code performs the following tasks:

It imports necessary libraries/modules: requests for making HTTP requests, BeautifulSoup from bs4 for web scraping, cv2 for image processing, os for interacting with the operating system, and pandas for handling data in a tabular format.

It defines two functions:

scrape_images(url): This function takes a URL as input, sends a GET request to that URL, parses the HTML content using BeautifulSoup, and extracts image URLs from <img> tags with the specified class name. It returns a list of image URLs.

resize_and_add_name(images): This function takes a list of image URLs as input, downloads each image, resizes it to 300x300 pixels using OpenCV (cv2), extracts the Pokemon name from the image URL, adds the Pokemon name as text on the image using OpenCV, saves the resized image, and returns a list of Pokemon names.

The main() function:

It specifies the URL of a webpage containing Pokemon images.
It calls the scrape_images() function to get a list of image URLs.
It calls the resize_and_add_name() function to download, resize, annotate with Pokemon names, and save the images.
It creates a pandas DataFrame containing the Pokemon names.
It saves the DataFrame to an Excel file.
Finally, it prints a message indicating that the images and names have been saved successfully.
The script checks if it's being run directly (__name__ == "__main__") and if so, it executes the main() function.
