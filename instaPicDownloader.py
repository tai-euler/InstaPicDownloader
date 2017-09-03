# needs to change interpreter to python 3.5+
# +++ download the high quality version of a instagram image +++
# author: Tai Euler -> steemit.com/@tai-euler
# command: python3 instaPicDownloader.py url
# example: python3 instaPicDownloader.py 'https://www.instagram.com/p/BPXMlaKj88u/?taken-by=wolfiecindy'

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from os.path import basename
import requests
import sys

try:
        # accept arguments -> the link to the instagram image
        my_url = sys.argv[1]
        # for manual URL deployment my_url = 'https://www.instagram.com/p/BPXMlaKj88u/?taken-by=wolfiecindy'
        print("Downloading from URL: " + my_url)

        # opening up connection, grabbing the page
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        # html parser
        page_soup = soup(page_html, "html.parser")

        # grabs the image source and save the link
        containers = page_soup.find("div", {"class" : "_4rbun"})
        image_source = containers.img["src"]

        # save image file in the same directory as you run the terminal
        f = open(basename(image_source), "wb")
        f.write(requests.get(image_source).content)
        print("High quality image downloaded from URL and saved as " + image_source)

except Exception as msg:
    print(msg)
