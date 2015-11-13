FROM centos:7

# set default workdir
RUN mkdir -p /usr/src/establishment_service/
WORKDIR /usr/src/establishment_service/

# Bundle app source and tests
COPY . /usr/src/establishment_service/

RUN yum install -y epel-release 
RUN yum install -y python34 gcc python34-devel \
 && curl https://bootstrap.pypa.io/get-pip.py | python3.4 - \
 && pip3.4 install pytest tornado pymongo==2.8.0 motor

# user to non-privileged user
# USER nobody
# Expose the application port and run application
EXPOSE 8888
CMD ["python3.4","app.py"]
