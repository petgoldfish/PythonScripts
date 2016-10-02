import urllib2
import json
import os
from sys import platform as sp


url = 'http://www.reddit.com/r/earthporn.json'

# Directory to save the images in
if sp == 'linux' or sp == 'linux2' or sp == 'darwin':
    directory = os.getenv('HOME')+'/Pictures/Walls'
else:
    directory = 'D:\Libraries\Pictures\Walls'


# Check if Directory already exists. If not then create a NEW dir
if not os.path.exists(directory):
    os.makedirs(directory)

hdr = {'User-Agent':
       ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 '
        '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
       'Accept':
       ('text/html,application/xhtml+xml,'
        'application/xml;q=0.9,*/*;q=0.8'),
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
page = urllib2.Request(url, headers=hdr)
response = urllib2.urlopen(page)
data = json.load(response)

for i in data["data"]["children"]:
    img_url = i["data"]["url"]
    try:
        if not str(img_url).endswith(".jpg"):
            img_url += '.jpg'
        if sp == 'linux' or sp == 'linux2' or sp == 'darwin':
            path = directory + "/" + str(img_url).split("/")[-1]
        else:
            path = directory + "\\" + str(img_url).split("/")[-1]
        # urllib.request.urlretrieve(img_url, path)
        print img_url
        urllib2.urlopen(img_url).read()
        output = open(path, 'wb')
        output.write(imgData)
        output.close()
    except:
        pass
