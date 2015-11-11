FROM centos:7

# set default workdir
WORKDIR /usr/src/establishment_service/

# Bundle app source and tests
COPY establishment_service/ /usr/src/establishment_service/

RUN yum install -y epel-release 
RUN yum install -y python34

# user to non-privileged user
# USER nobody
# Expose the application port and run application
EXPOSE 8888
CMD [“python3.4”,”app.py”]
