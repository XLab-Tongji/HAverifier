# HAverifier
HA Verification System for Cloud Platform

# Install
## Centos
sudo yum install -y python-pip.noarch
sudo yum install -y gcc libffi-devel python-devel openssl-devel
sudo cp -a pod.yaml /etc/haverifier/pod.yaml
sudo ./setup.py install
## Ubuntu
sudo apt-get install -y python-pip
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
sudo cp -a pod.yaml /etc/haverifier/pod.yaml
sudo ./setup.py install
