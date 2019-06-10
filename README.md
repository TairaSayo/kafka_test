# Test deployment Kafka and Prometheus using Vagrant and VirtualBox

## Layout

1. Solution create and setup three VM: kafka, worker, prometheus
2. kafka VM settings:
    - Host name - kafka
    - IP - 10.10.0.100
    - Installed services - Kafka, Node_exporter, JVM_exporter
3. worker VM settings:
    - Host name - worker
    - IP - 10.10.0.101
    - Installed services - Input(kafka producer), Output(kafka consumer), Node_exporter
4. prometheus VM settings:
    - Host name - prometheus
    - IP - 10.10.0.102
    - Installed services - Prometheus, Node_exporter, Grafana

## Requiremets

- Vagrant 2.2.3
- VM Virtual box 6.0
- 10.10.0.0/24 network is not used on host
- Host machine with internet connecton
### Warning: solution was tested on Windows based host only!

## To start

```bash
- clone repository:
git clone https://github.com/TairaSayo/kafka_test.git
- run deployment
cd ./kafka_test
vagrant up
```

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

### Created for testing purporces only, do not use in live invironment!
