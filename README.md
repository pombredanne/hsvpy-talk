hsvpy-talk
==========

HSV python group intro to django talk on May 13, 2014

The slides from the talk are in google presentation format at http://goo.gl/1fX0j9

The seed template for the django project comes from https://github.com/twoscoops/django-twoscoops-project

To get this running on your machine, you will need virtualenv installed

```
$ git clone https://github.com/mark0978/hsvpy-talk.git hsvpy
$ cd hsvpy
$ virtualenv .hsvpy
$ source .hsvpy/bin/activate                     # leave off the source word for windows
(.hsvpy)$ pip install -r requirements/local.txt
(.hsvpy)$ export DJANGO_SETTINGS=hsvpy.settings.local    # change export to set for windows   
(.hsvpy)$ python manage.py syncdb
(.hsvpy)$ python manage.py runserver
```

open your browser and visit http://localhost:8000/stories/

