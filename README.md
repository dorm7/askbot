# INSTALLATION

pip install -r requirements.txt

    python manage.py syncdb
    python manage.py migrate askbot
    python manage.py migrate django_authopenid
    python manage.py migrate
    python manage.py runserver

# MODIFICATION

The skins file are in *skins/foxconn/* , you can modify templates and media files here. To know more about askbot skins. To know more about askbot skins, you can reference [here](http://askbot.org/doc/customizing-skin-in-askbot.html)
