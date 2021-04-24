Prerequisites
you will need:

an AWS account with the IAM permissions listed on the EKS module documentation (or Admin access),
a configured AWS CLI
AWS IAM Authenticator
kubectl
wget (required for the eks module)
helm

git clone https://github.com/almogTsarfati/vcita.git
cd vcita
terraform init
terraform apply
aws eks --region $(terraform output -raw region) update-kubeconfig --name $(terraform output -raw cluster_name)

helm install my-chart app-chart/
