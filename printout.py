from os.path import join, basename
from glob import glob
import json
PICS_DIR = 'pics'
RECOG_DIR = 'responses'


HTML_FILENAME = 'printout.html'
htmlfile = open(HTML_FILENAME, 'w')
htmlfile.write("<html><title>Hello</title><body>")
htmlfile.write("<h1>Hi, these are my photos</h1>")


for jsonname in glob(join(RECOG_DIR, '*.json')):
    print("Extracting", jsonname)
    j = json.load(open(jsonname))
 
    img = j['images'][0]
    
    imgname = img['image']
    htmlfile.write("<h2>%s</h2>" % imgname)

    imgfilename = join(PICS_DIR, imgname)
    
    htmlfile.write('<img src="%s">' % imgfilename)
    
    myimageslist = []

    numitems = len(img["scores"])
    for item in range(numitems):
        myimageslist.append("<p>" + str(item +1) + str(img["scores"][item]["classifier_id"]) + str(img["scores"][item]["score"]) + "<p>")


    for x in myimageslist:
        htmlfile.write(x)


htmlfile.close()