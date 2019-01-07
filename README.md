# prism-challenge
Set up a K8s cluster in AWS using Terraform and Ansible. Then deploy a Python API

Prerequisites: Vangrant and VirtualBox


This is just a proof of concept. This project is not intended to production.

How to use it:

Create the EKS-Cluster

1 - Create a IAM user using the AWS console and give the relevant privileges

2 - clone this repository

3 - cd into the project root

4 - run the command -- vagrant up

5 - sudo into the terraform user -- sudo -iu terraform

6 - cd into the eks-cluster directory

7 - export your IAM credentials

export AWS_ACCESS_KEY_ID=<-- Replace with your credentials -->

export AWS_SECRET_ACCESS_KEY=<-- Replace with your credentials -->

8 - run -- terraform init

9 - run -- terraform apply

The above should create a fully operational EKS cluster with 2 nodes

Configure Kubectl to work with your recent created cluster.

1 - run -- terraform output kubeconfig

2 - copy the output to /home/terraform/.kube/config

3 - run -- terraform output config-map-aws-auth

4 - create a file called config-map-aws-auth.yaml

5 - copy the output to config-map-aws-auth.yaml

6 - run -- kubectl apply -f config-map-aws-auth.yaml

You should be connected to the cluster to test it run kubectl get nodes

Deploy Tiller to the cluster (Optional)

Those steps are only required if you want to use helm

1 - run -- kubectl create serviceaccount tiller --namespace kube-system

2 - run -- kubectl apply -f k8s-eks/rbac-config.yaml

3- run -- helm init --service-account tiller

To test it run -- kubectl get pods --namespace kube-system | grep tiller

Deploy the API
from the root of the project run -- helm install --debug api-chart/ --name prism
