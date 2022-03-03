import links
import emails_numbers
import hashes
import requests
import images
from bs4 import BeautifulSoup
import sys


def main():
    ''' Retrieve a webpage via with user input and return its contents'''


while True:
    try:
        user_url = input("Enter Url ")
        get_html = requests.get(user_url)  # Make request to web page
        soup = BeautifulSoup(get_html.text, "html.parser") # create beautifulsoup object
        str_var = str(soup)  
    except ValueError:
        print('Invalid URL - Must start with http://')
        continue
    except KeyboardInterrupt:
        print('Stopping Program - Ctrl C is great isnt it?')
        sys.exit(0)

    # call functions
    links.print_links(soup)
    emails_numbers.find_email(soup)
    emails_numbers.phone_numbers(soup)
    hashes.get_hashes(soup)
    hashes.get_images(soup)
    hashes.get_docs(soup)
    # images.imagefiles(soup,user_url)
