#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install -y git python-pip python-setuptools python-blist

cd /opt

sudo git clone https://github.com/jdiazfernandez/tfc_iot_ha.git

sudo pip install bravado flask click

python /opt/tfc_iot_ha/src/anomaly_detection.py &