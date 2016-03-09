import requests
import os
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)

URLS = ['https://upload.wikimedia.org/wikipedia/commons/f/f6/Bulgarian_Muslims_from_Rhodopes_%281932%29.jpg',
	'http://blackwhite.io/wp-content/uploads/2016/01/Street-Road-Infinity-970x970.jpg',
	'https://freeimages.red/static2/preview2/photo-jellyfish-12265.jpg',
	'https://freeimages.red/static2/preview2/photo-sweet-table-12691.jpg',
	'https://freeimages.red/static2/preview2/photo-sunset-eiffel-tower-12740.jpg',
	'https://freeimages.red/static2/preview2/photo-halfdome-yosemite-national-park-10827.jpg',
	'https://freeimages.red/static2/preview2/photo-indonesia-volcanos-8537.jpg']

numUrls = len(URLS) 

for url in range(numUrls):
    print("Downloading", URLS[url])
    resp = requests.get(URLS[url])
    # url = url.replace('/', '-')
    picname = "pic" + str(url)     
    fname = os.path.join(PICS_DIR, picname)
    print("Saving to", fname)
    f = open(fname, 'wb')
    f.write(resp.content)
    f.close()
