# install asnible
apt install python3-pip
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
#set up asnible
ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml