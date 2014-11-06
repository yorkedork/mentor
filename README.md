# MAPS Mentor Webform 
## Install
Go to mentor directory, install neccessary softwares for the project

    virtualenv --no-site-packages -p /usr/bin/python3 .env
    source .env/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py loaddata choices
    ./manage.py collectstatic --no-input
    

    
Create a local copy of the example settings, and configure the SECRET_KEY and DB config

    cp mentor/settings/local.py.template mentor/settings/local.py
    vi mentor/settings/local.py
    
Change some settings for the website in base.py such as EMAIL_LIST

    vi mentor/settings/base.py

