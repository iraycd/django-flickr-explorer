"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
import urllib2
import StringIO
import json

def downloadImage(url="http://farm9.staticflickr.com/8386/8683252171_335d868570_b.jpg",fileName=False):
    from PIL import Image
    from urlparse import urlparse
    if fileName==False:
        fileName = (url.split('/')[-1]).split('.')[0]
    img = urllib2.urlopen(url).read()
    im = Image.open(StringIO.StringIO(img)).convert("RGB")
    im.save("images/" +fileName + ".jpg", "JPEG",quality=100)
    print("Done!!!")


def downloadFlickr(data):
    photos = data['photos']['photo']
    print("Images : " +str(len(photos)))
    for photo in photos:
        pid = str(photo['id'])
        owner = str(photo['owner'])
        secret = str(photo['secret'])
        server = str(photo['server'])
        farm   = str(photo["farm"])
        title  = photo["title"]
        url = "http://farm"+farm+".staticflickr.com/"+server+"/"+pid+"_"+secret+"_b.jpg"
        print(url)
        print("Downloading....")
        try:
            downloadImage(url=url,fileName=title)
        except:
            downloadImage(url=url) 

def getFlickr(
        url = "http://api.flickr.com/services/rest?method=flickr.interestingness.getList&api_key=4f0730d565d764ed48a99cba3148fcfb&format=json&nojsoncallback=1&per_page=500"
    ):
    n = urllib2.urlopen(url).read()
    data= json.loads(n)
    downloadFlickr(data)

def offlineFlickr(fileName = "flickr.json"):
    json_file = open(fileName)
    data = json.load(json_file)
    downloadFlickr(data)
     