from urllib.request import urlopen
import urllib
import json
import os

url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=5&mkt=en-US'

# Directory to save the images in
directory = 'D:\Libraries\Pictures\Walls'

# Check if Directory already exists. If not then create a NEW dir
if not os.path.exists(directory):
    os.makedirs(directory)

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Wall_getter_guy')]
response = opener.open(url)
data = json.loads(response.read().decode('utf-8'))

for i in data["images"]:
    img_url = i["urlbase"]

    try:
        full_url = 'http://bing.com' + img_url + '_1920x1080.jpg'

        path = directory + "\\" + str(full_url).split("/")[-1]

        urllib.request.urlretrieve(full_url, path)

    except:
        pass