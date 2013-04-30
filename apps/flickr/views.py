# Create your views here.
import json
from django.http import HttpResponse,Http404
from .models import Image, FlickUser 
from django.views.generic.list import ListView

class ImageListView(ListView):
    model = Image
    template_name ="home.html"
    context_object_name = 'images'

def getImage(request):
    import urllib2
    api_key = "46687c883e0bb90a4d77ef32a94e9154"
    per_page = "50"
    url = "http://api.flickr.com/services/rest/?method=flickr.interestingness.getList&api_key="+api_key+"&per_page="+per_page+"&extras=+description%2C+license%2C+date_upload%2C+date_taken%2C+tags%2C+machine_tags%2C++media%2C+path_alias%2C+url_o%2C+owner_name&format=json&nojsoncallback=1"
    n = urllib2.urlopen(url).read()
    data= json.loads(n)
    jsondata = json.dumps(data)
    photos = data['photos']['photo']
    for photo in photos:
        u = None
        try:
            u = FlickUser.objects.get(owner=photo['owner'])
        except:
            u = FlickUser(name=photo['ownername'],owner=photo['owner'],username=photo['pathalias'])
            u.save()
        downloadFlickr(photo,u)
    return HttpResponse(jsondata,mimetype='application/json')


def downloadFlickr(photo,u):
    image = None
    pid = str(photo['id'])
    secret = str(photo['secret'])
    server = str(photo['server'])
    farm   = str(photo["farm"])
    try:
        url = photo['url_o']
    except:
        url = "http://farm"+farm+".staticflickr.com/"+server+"/"+pid+"_"+secret+"_b.jpg"
    try:
        image = Image.objects.get(photo_id=photo['id'])
        return None
    except:
        image = Image(photo_id=pid,title = photo["title"], image_url = url, owner = u, description = photo['description'])
        image.save()
        from django.core.files.uploadedfile import InMemoryUploadedFile
        from PIL import Image as ImageObj
        import cStringIO , StringIO , base64
        import urllib2
        fileName = (url.split('/')[-1]).split('.')[0]
        img = urllib2.urlopen(url).read()
        im = ImageObj.open(StringIO.StringIO(img)).convert("RGB")
        tempfile_io =StringIO.StringIO()
        im.save(tempfile_io,'JPEG')
        image_file = InMemoryUploadedFile(tempfile_io, None, 'rotate.jpg','image/jpeg',tempfile_io.len, None)
        image.picture.save(fileName+".jpg", image_file , save=True)

