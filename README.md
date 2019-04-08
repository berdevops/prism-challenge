# Set up a K8s clusterusing(EKS) with Terraform and Ansible. Then deploy a Python API

## Info

Prerequisites: Vangrant and VirtualBox

- This is just a proof of concept. This project is not intended to production.

* [VirtualBox] - Virtualization tool
* [Vagrant] - The development environment build tool.

## How to use it:
Vagrant and Virtualbox are going to spin a Centos VM locally. Then Ansible will install all the dependencies for this project in this VM. Once the installation is finished, ssh into the VM and you are ready to create the cluster using Terraform and operate it using kubectl.

### Create the EKS-Cluster

- Create a IAM user using the AWS console and give the relevant privileges
- clone this repository
- cd into the project root
- run vagrant up
```sh
git clone http://repository.url
cd terraform-eks/
vagrant up
```
- ssh into the VM
```sh
vagrant ssh
```
sudo into the terraform user
```sh
sudo -iu terraform
```
- cd into the eks-cluster directory
- export your IAM credentials
```sh
export AWS_ACCESS_KEY_ID=<-- Replace with your credentials -->
export AWS_SECRET_ACCESS_KEY=<-- Replace with your credentials -->
```
- run 
```sh
cd eks-cluster/

// first
terraform init

// second
terraform apply
``` 
The above should create a fully operational EKS cluster with 2 nodes

### Configure Kubectl to work with your recent created cluster.

- run
```sh
terraform output kubeconfig
```
- copy the output to /home/terraform/.kube/config
- create a file called config-map-aws-auth.yaml (mind the path for this file in your next command) 
- run
```sh
terraform output config-map-aws-auth
```
- copy the output to config-map-aws-auth.yaml
- run
```sh
kubectl apply -f config-map-aws-auth.yaml
```
You should be connected to the cluster to test it run kubectl get nodes
```sh
kubectl get nodes
```

### Deploy Tiller to the cluster (Optional)

Those steps are only required if you want to use helm

- run
```sh
kubectl create serviceaccount tiller --namespace kube-system
```
- run
```sh
kubectl apply -f k8s-eks/rbac-config.yaml
```
- run 
```sh
helm init --service-account tiller
```
- To test it run
```sh
kubectl get pods --namespace kube-system | grep tiller
```

### Deploy the API

- from the root of the project run
```sh
helm install --debug api-chart/ --name example
```
