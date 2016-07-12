from urllib.request import urlopen
import urllib
import json
import os

url = 'http://www.reddit.com/r/earthporn.json'

# Directory to save the images in
directory = 'D:\Libraries\Pictures\Walls'

# Check if Directory already exists. If not then create a NEW dir
if not os.path.exists(directory):
    os.makedirs(directory)

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Raghavsai_guy')]
response = opener.open(url)
data = json.loads(response.read().decode('utf-8'))

for i in data["data"]["children"]:
    img_url = i["data"]["url"]
    try:
        if not str(img_url).endswith(".jpg"):
            img_url += '.jpg'
        path = directory + "\\" + str(img_url).split("/")[-1]
        urllib.request.urlretrieve(img_url, path)
    except:
        pass