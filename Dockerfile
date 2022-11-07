#Download base image ubuntu 20.04
FROM ubuntu:20.04

#update 
RUN apt-get update

RUN apt-get install -y vim traceroute net-tools iputils-ping netbase curl sudo

RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.8 python3-pip

# ADD . /export
COPY . /export
# WORKDIR /export

# RUN chmod +x entry.sh
# ENTRYPOINT ["./entry.sh","/bin/bash"]
# CMD python3 src/app.py src/data/capk.yaml
