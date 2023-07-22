import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

var = int(input("enter count: "))
vart = int(input("enter position: "))

responses = []
urls = []

for click in range(0, var):
    tags = soup('a')
    target_url = tags[vart-1]['href']
    urls.append(target_url)
    response = requests.get(target_url)
    responses.append(response)
    soup = BeautifulSoup(response.text, 'html.parser')

final_url = urls[-1]
name_match = re.search(r'_by_([^/]+)\.html$' , final_url)
name = name_match.group(1)
print("Name from the last URL: ", name)
    