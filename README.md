# Test deployment Kafka and Prometheus using Vagrant and VirtualBox

## Request

Use Vagrant, Ansible to provision 3 VMs (Centos7);
Install and configure Kafka on VM1 (with Ansible);
Create topics on Kafka 'input', 'output';
Create solution 1 that produces epoch timestamp in ms to 'input' once per second;
Create solution 2 that consumes from topic 1, transforms input message to date string (RFC 3339), sends to topic 'output';
Deploy both solutions to VM2. They should both be managed as systems services.
In VM3 install Prometheus, Grafana. Find a way to export Kafka metrics and metric from solutions 1,2 and visualize them in Grafana.

## Layout

1. Solution create and setup three VM: kafka, worker, prometheus
2. kafka VM settings:
    2.1 Host name - kafka
    2.2 IP - 10.10.0.100
    2.3 Installed services - Kafka, Node_exporter, JVM_exporter
3. worker VM settings:
    2.1 Host name - worker
    2.2 IP - 10.10.0.101
    2.3 Installed services - Input(kafka producer), Output(kafka consumer), Node_exporter
4. prometheus VM settings:
    2.1 Host name - prometheus
    2.2 IP - 10.10.0.102
    2.3 Installed services - Prometheus, Node_exporter, Grafana

## Requiremets

Vagrant 2.2.3
VM Virtual box 6.0
10.10.0.0/24 network is not used on host
Host machine with internet connecton
Warning: solution was tested on Windows based host only!

## To start

- clone repository:
git clone https://github.com/TairaSayo/kafka_test.git
- run deployment
cd ./kafka_test
vagrant up

## To remove

vagrant destroy -f

## Access points

- Prometheus dashboard

```bash
http://10.10.0.102:9090
or
http://localhost:9090
```

- Grafana dashboard (user: admin; password: admin)

```bash
http://10.10.0.102:3000/d/2P-hCZnWk/solution-overview
or
http://localhost:3000/d/2P-hCZnWk/solution-overview
```

- hosts metrics

```bash
worker:
http://10.10.0.101:9100 > System metrics
http://10.10.0.101:8000 > Producer metrics
http://10.10.0.101:8100 > Consumer metrics

kafka:
http://10.10.0.100:9100 > System metrics
http://10.10.0.100:7071 > Kafka metrics

promethius:
http://10.10.0.102:9100 > System metrics
```

# Created for testing purporces only, do not use in live invironment!