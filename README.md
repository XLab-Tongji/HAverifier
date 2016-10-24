# HAverifier
HA Verification System for Cloud Platform.

HAVerifer is designed to run software based fault
injection and HA test cases on multiple HA topologies of
OpenStack. The general design principles include scenariodriven, configurable-based automation, state restoration, loose
coupling, high cohesion and universal compatibility. The test
case for this framework are defined in a YAML configuration
file, the FIR are written in shell scripts, the testers design a test
case by orchestrating the steps in the YAML file. Such a design
makes the framework easy for the testers to use.

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
