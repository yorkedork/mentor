###############################
#                             #
#  Mentor                     #
#  Ubuntu 14.10 Docker Image  #
#                             #
###############################
FROM ubuntu:latest
MAINTAINER Thom Linton <tlinton@pdx.edu>
VOLUME /opt/host/

# Add docker assets to container
COPY /assets /usr/local/docker/
COPY /bin /usr/local/docker/bin

# Install repositories, dependencies and update system packages
RUN /usr/local/docker/bin/install_dependencies.sh

# System property configuration
RUN /usr/local/docker/bin/configure_system.sh

# Environment and entry-point configuration
COPY entrypoint.sh /usr/local/docker/
ENTRYPOINT ["/usr/local/docker/entrypoint.sh"]
