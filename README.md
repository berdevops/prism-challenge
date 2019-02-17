# Set up a K8s clusterusing(EKS) with Terraform and Ansible. Then deploy a Python API

## Info

Prerequisites: Vangrant and VirtualBox

* [VirtualBox] - Virtualization tool
* [Vagrant] - The development environment build tool.

## How to use it:

- This is just a proof of concept. This project is not intended to production.

### Create the EKS-Cluster

- Create a IAM user using the AWS console and give the relevant privileges
- clone this repository
- cd into the project root
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
- run
```sh
terraform output config-map-aws-auth
```
- create a file called config-map-aws-auth.yaml
- copy the output to config-map-aws-auth.yaml
- run
```sh
kubectl apply -f config-map-aws-auth.yaml
```
You should be connected to the cluster to test it run kubectl get nodes

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
helm install --debug api-chart/ --name prism
```
