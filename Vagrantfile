Vagrant.configure("2") do | config |
  config.vm.define 'kafka' do | kafka |
    kafka.vm.box = "centos/7"
    kafka.vm.synced_folder "./kafka/", "/vagrant", owner: "vagrant", mount_options: ["dmode=775,fmode=775"]
    kafka.vm.hostname = 'kafka'
    kafka.vm.network "private_network", ip: "10.10.0.100"
    kafka.vm.provision "ansible_local" do |ansible|
      ansible.become = true
      ansible.playbook = "kafka_ansible.yml"
      end
    kafka.vm.provider :virtualbox do |vb|
      vb.name = "vm1"
      vb.customize ["modifyvm", :id, "--memory", 2048]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.gui = false
    end
  end
  config.vm.define 'worker' do | worker |
    worker.vm.box = "centos/7"
    worker.vm.synced_folder "./worker/", "/vagrant", owner: "vagrant", mount_options: ["dmode=775,fmode=775"]
    worker.vm.hostname = "worker"
    worker.vm.network "private_network", ip: "10.10.0.101"
    worker.vm.provision "ansible_local" do |ansible|
      ansible.become = true
      ansible.playbook = "worker_ansible.yml"
      end
    worker.vm.provider :virtualbox do |vb|
      vb.name = "vm2"
      vb.customize ["modifyvm", :id, "--memory", 512]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.gui = false
    end
  end
  config.vm.define 'prometheus' do | prometheus |
    prometheus.vm.box = "centos/7"
    prometheus.vm.synced_folder "./prometheus/", "/vagrant", owner: "vagrant", mount_options: ["dmode=775,fmode=775"]
    prometheus.vm.hostname = "prometheus"
    prometheus.vm.network "private_network", ip: "10.10.0.102" 
    prometheus.vm.network :forwarded_port, guest: 9090, host: 9090
    prometheus.vm.network :forwarded_port, guest: 9100, host: 9100
    prometheus.vm.provision "ansible_local" do |ansible|
      ansible.become = true
      ansible.playbook = "prometheus_ansible.yml"
      end
    prometheus.vm.provider :virtualbox do |vb|
      vb.name = "vm3"
      vb.customize ["modifyvm", :id, "--memory", 1024]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.gui = false
    end
  end 
end
