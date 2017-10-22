#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install -y python-pip build-essential python-dev libffi-dev libssl-dev 

sudo pip install -U setuptools

sudo pip install elastalert

cp /vagrant/conf/config.yaml /home/vagrant

cp /vagrant/conf/uuid_rule.yaml /home/vagrant

python -m elastalert.elastalert --verbose --config /home/vagrant/config.yaml --rule /home/vagrant/uuid_rule.yaml &