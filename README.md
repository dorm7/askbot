# INSTALLATION

pip install -r requirements.txt

PS: please follow the steps correctly

    cd foxconn
    python manage.py syncdb
    python manage.py migrate askbot
    python manage.py migrate django_authopenid
    python manage.py migrate
    python manage.py runserver

# Settings

In order to use the tumblr api, you need to set TUMBLR_CONSUMER_KEY in settings.py. To know more about TUMBLR API, you can view [Tumblr API](http://www.tumblr.com/docs/en/api/v2) to get information.

After You get your key, you can specify TUMBLR_SITE, It is the tumblr site's domain name, such as blog.krdai.info. 

# MODIFICATION

The skins file are in *skins/foxconn/* , you can modify templates and media files here. To know more about askbot skins. To know more about askbot skins, you can reference [here](http://askbot.org/doc/customizing-skin-in-askbot.html)

