# DevOps4IoTProject
The DevOps4IoT framework provides an architecture for a centralized monitoring infrastructure that allows developers to obtain fast and continuous feedback from operation, specifically to detect anomalies to better anticipate problems when a production deployment is performed. The instantiation of this architecture is described through a case study that shows the versioned and repeatable configuration of the monitoring infrastructure (Infrastructure as Code) through virtualization and containerization technology.

To execute this framework and demo, Vagrant has to be previously installed (see https://www.vagrantup.com/intro/getting-started/install.html). 

Next, run the following from your terminal to boot two Vagrant environments: 

(//YOUR PATH//dockers)$ vagrant up

(//YOUR PATH//elastalert)$ vagrant up

Note: It is important to boot the first environment before the second one. 


Next, you can test the framework

Portainer: http://localhost:9900/  -> You can see all running docker containers 

haproxy: http://localhost:8080/haproxy?stats -> You can monitor the Orion Context Broker nodes

ElasticSearch: http://localhost:9200 --> you can see the indices logstash-* and elastalert_status (this last one monitors an anomaly)

Kibana: http://localhost:5601 --> you can configure index patterns (i.e. logstash-* and elastalert_status) to visualize the search 

Demo: http://localhost:5000/ --> You can execute this simulator to create entities (devices) that send messages to Orion Context Broker nodes and create an anomaly to validate the framework is working

