Hello!

You will need:
an AWS account with the IAM permissions listed on the EKS module documentation (or Admin access),
a configured AWS CLI
AWS IAM Authenticator
kubectl
wget (required for the eks module)
helm

Run the following commands:
git clone https://github.com/almogTsarfati/vcita.git
cd vcita
terraform init
terraform apply
aws eks --region $(terraform output -raw region) update-kubeconfig --name $(terraform output -raw cluster_name)
helm install my-chart app-chart/

Run this command to get one of the k8s nodes public IP:
aws ec2 describe-instances | grep PublicIp
Run this command to get the exposed port:
kubectl describe svc vcita-service | grep NodePort

Finaly, Run:
curl -X POST --data "Hi!" <node-public-ip>:<port>