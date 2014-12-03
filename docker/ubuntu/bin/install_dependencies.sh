#
# NOTES:
#   Use vagrant to provision basic 'host' (what UNIX team would provide)
#
#   Services would be provided by network infrastructure or host VM and
#   configured appropriately. Host will provide these services as well as
#   forwarding rules.
#
#   So, VM becomes development host; docker container should be equivalent
#   across deployments to production and development VM hosts.
#
#   Application-level needs and application adapter should be installed
#   to target Docker container.

# Refresh local APT cache
apt-get update

# Install system packages
apt-get install -y \
    ntp \
    openssh-server \
    emacs24-nox \
    git \
    tar unzip

# Install project build dependencies
apt-get install -y \
    python3-all python3-all-dev \
    python-virtualenv

# Install MySQL
apt-get install -y \
    mysql-server \
    mysql-client

# Install Httpd
apt-get install -y \
    apache2 libapache2-mod-wsgi-py3
cp /usr/local/docker/conf/httpd/vhost.d/mentoring.local.conf \
    /etc/apache2/sites-available
a2ensite mentoring.local

# Update all installed packages
apt-get -y upgrade
