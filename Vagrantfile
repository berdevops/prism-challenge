
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
    config.vm.define "terraformChallenge"
    config.vm.box = "geerlingguy/centos7"

    # KNOWN ISSUE WITH VAGRANT 1.8.5 - https://github.com/mitchellh/vagrant/issues/7610
    config.ssh.insert_key = false

    #config.vm.network :forwarded_port, guest: 80, host: 8000
    config.ssh.forward_agent = true

    config.vm.synced_folder ".", "/home/terraform/challenge", id: "project-root", :owner => "4665", :group => "4665"

    # ansible_local runs Ansible from inside the Vagrant
    config.vm.provision "ansible_local" do |ansible|
        ansible.groups = {
            "local" => ["terraformChallenge"]
        }
        ansible.playbook = "ansible/set-up.yml"
        ansible.provisioning_path = "/home/terraform/challenge"
    end

    # Vm config
    config.vm.provider :virtualbox do |vb|
	    vb.customize ["modifyvm", :id, "--memory", "4192"]
    end
end