## Kafka/Zookeeper (kafka directory)

### Prequisite

Install `terraform-inventory`: https://github.com/adammck/terraform-inventory

```shell
# Ensure go is installed
$ go --version
$ go get github.com/adammck/terraform-inventory
$ go install github.com/adammck/terraform-inventory
$ mv ~/go/bin/terraform-inventory /usr/local/bin/terraform-inventory
```

### Bootstrap Kafka/Zookeeper cluster

1. Copy `terraform.tfstate` from `terraform` directory
2. Run `./gen_inventory.sh`
3. Commit and push your code.
4. SSH into bastion server.
5. Update repo.
6. run `ansible-playbook playbooks/kafka_and_zoo.yaml`

## Consul/Nomad/Gitlab Runner/Configuration/Operation (app directory)

### To boostrap Consul Cluster

1. Copy `terraform.tfstate` from `terraform` directory
2. Run `./inventory_builder.py`
3. Commit and push your code.
4. SSH into bastion server.
5. Update repo.
6. run `ansible-playbook playbooks/common.yaml`
7. run `ansible-playbook playbooks/consul.yaml`

### To boostrap Nomad Cluster

1. Copy `terraform.tfstate` from `terraform` directory
2. Run `./inventory_builder.py`
3. Commit and push your code.
4. SSH into bastion server.
5. Update repo.
6. run `ansible-playbook playbooks/common.yaml`
7. run `ansible-playbook playbooks/consul.yaml`
8. run `ansible-playbook playbooks/nomad/cni.yml`
9. run `ansible-playbook playbooks/nomad.yaml`

### To add new worker node (aka. Nomad agent node)

1. Copy `terraform.tfstate` from `terraform` directory
2. Run `./inventory_builder.py`
3. Commit and push your code.
4. SSH into bastion server.
5. Update repo.
6. run `ansible-playbook playbooks/common.yaml -l <new_node_ip>`
7. run `ansible-playbook playbooks/consul.yaml -l <new_node_ip>`
8. run `ansible-playbook playbooks/nomad/cni.yml -l <new_node_ip>`
9. run `ansible-playbook playbooks/nomad.yaml -l <new_node_ip>`
10. Check by using Nomad UI (see Tips)

### To add new gitlab-runner node

1. Copy `terraform.tfstate` from `terraform` directory
2. Run `./gen_inventory.sh`
3. Commit and push your code.
4. SSH into bastion server.
5. Update repo.
6. run `ansible-playbook playbooks/common.yaml -l <new_node_ip>`
7. run `ansible-playbook playbooks/consul.yaml -l <new_node_ip>`
8. run `ansible-playbook playbooks/gitlab-runner.yaml -l <new_node_ip>`

## Tips

SSH:

```shell
ssh -L 8500:<consul0_ip>:8500 -L 4646:<nomad0_ip>:4646 <bastion_host_ip>
```

Then:

- [http://127.0.0.1:4646](http://127.0.0.1:4646) will be Nomad UI
- [http://127.0.0.1:8500](http://127.0.0.1:8500) will be Consul UI
