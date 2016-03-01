FROM ubuntu:latest
RUN apt-get -y update && apt-get install -y aptitude && apt-get install -y python-pip
RUN pip install django
RUN apt-get update
RUN apt-get install -y  python-numpy
RUN apt-get install -y python-scipy
RUN apt-get install -y python-mysqldb
RUN apt-get install -y git
CMD cd /home && git clone https://github.com/gymgithub/gym-web.git

