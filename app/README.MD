# Setup

### Install ansible
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
### Update dependencies
```shell
$ ansible-galaxy install -r requiment.yaml
```

### Explain

- bastion.yaml: Setup bastion host
- fcm.yaml: Setup FCM config inside Consul
- mysql.yaml: Manage and Set MySQL config inside Consul
- postgres.yaml: Manage and Set Postgres config inside Consul
- redis.yaml: Setup Redis config inside Consul
- s3.yaml: Setup S3 config inside Consul
- zookeeper.yaml: Setup Config inside Zookeeper

### To add nomad node
```shell
$ ansible-playbook bootstrap-nomad-node.yaml -e nomad_hosts=<new_node_ip>
```