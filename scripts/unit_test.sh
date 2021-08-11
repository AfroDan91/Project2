#! /bin/bash

#install dependencies
sudo apt update
sudo apt-get install python3 python3-pip python3-venv -y
# create and activate venv
python3 -m venv venv
source venv/bin/activate
# install reqs
pip3 install -r requirements.txt
#run tests with cov reports
python3 -m pytest --cov=.  
