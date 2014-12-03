#!/bin/bash

#
# Start necessary system services
#
service mysql start
service apache2 start

#
# Unpack codebase and bootstrap application
#
BASE_PATH="/webapps"
PROJECT="mentor"
VERSION=$1 || "master"

if [ ! -d "${BASE_PATH}" ]; then
  mkdir ${BASE_PATH}
  cd ${BASE_PATH}
  git clone file:///opt/host/${PROJECT} ${PROJECT}

  cd ${PROJECT}
  git remote set-url origin https://github.com/PSU-OIT-ARC/mentor.git
  echo "Checking out version $1..."
  git checkout "$1"
  echo "Cloning configuration..."
  cp /opt/host/${PROJECT}/${PROJECT}/local_settings.py ${PROJECT}/local_settings.py
  echo "Bootstrapping..."
  virtualenv --python=python3 --no-site-packages env
  source env/bin/activate
  pip install -r requirements.txt
  mysql -u root -e "CREATE DATABASE IF NOT EXISTS mentor"
  mysql -u root -e "CREATE USER mentor IDENTIFIED BY 'mentor'"
  mysql -u root -e "GRANT ALL ON mentor.* TO 'mentor'"
  ./manage.py migrate
  ./manage.py loaddata choices  
  ./manage.py loaddata users
  ./manage.py collectstatic

  chown -R www-data:www-data ${BASE_PATH}/${PROJECT}
fi

exec /bin/bash
