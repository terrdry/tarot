[ Installing Virtual environment for Ansible and Terraform molecule testing ](./docs/vagrant.md)

molecule init scenario webapp

This will create the following structure

```bash
.
./molecule
./molecule/tarot
./molecule/tarot/molecule.yml
./molecule/tarot/converge.yml
./molecule/tarot/create.yml
./molecule/tarot/destroy.yml
```

And runs the above playbook to do the testing

ansible-galaxy role init mywebapp

# config.vm.provision "shell", inline: <<-SHELL

    #   sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
    #   wget -O- https://apt.releases.hashicorp.com/gpg | \
    #   gpg --dearmor | \
    #   sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

    #   echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    #   https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    #   sudo tee /etc/apt/sources.list.d/hashicorp.list

    #   sudo apt update
    #   sudo apt-get install terraform

    # SHELL

.
├── ansible.cfg
├── group_vars
│   ├── mysql-servers
│   │   └── main.yml
│   └── nginx-servers
│       └── main.yml
├── inventory
│   └── prod.ini
├── roles
│   ├── mysql
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── templates
│   │   │   └── mytemplate.j2
│   │   └── vars
│   │       └── main.yml
│   └── nginx
│       ├── tasks
│       │   └── main.yml
│       ├── templates
│       │   └── mytemplate.j2
│       └── vars
│           └── main.yml
|       .
|       .
└── setup.yml

inventories/
production/
hosts               # inventory file for production servers
group_vars/
group1.yml       # here we assign variables to particular groups
group2.yml
host_vars/
hostname1.yml    # here we assign variables to particular systems
hostname2.yml

staging/
hosts               # inventory file for staging environment
group_vars/
group1.yml       # here we assign variables to particular groups
group2.yml
host_vars/
stagehost1.yml   # here we assign variables to particular systems
stagehost2.yml

library/
module_utils/
filter_plugins/

site.yml
webservers.yml
dbservers.yml

roles /
common/
webtier/
monitoring/
fooapp/
