Django flickr explorer
======================

This app was developed just for fun.

What this app do?
-----------------
Get all the popular images from flickr explorer section. Using Flickr API.
API is pretty simple to understand.


Installation and Setup:
-----------------------

```sh
git clone https://github.com/iraycd/django-flickr-explorer.git
cd django-flickr-explorer
python manage.py syncdb
python manage.py runserver
```

  - Change the api_key at /apps/flick/views.py to your api_key
  - Change the per_page default is set to '50' the max is '500'

How does it work?
-----------------
 - To get images go to "/get"
 - You can see the details using django admin.
 - You can view the images on the home page.

Worst thing i have done during the design?
------------------------------------------
 - Din't use thumbnails.
 - Getting the Original images.(Even if the image is 7MB+ it will be loaded)
 - Din't compress the image.
 - Din't write proper code for getting different image sizes.
 - Din't maintain a base.html.
 - Din't keep the api_key in settings.py


