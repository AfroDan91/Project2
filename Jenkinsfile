pipeline{
        agent any
        stages{
            stage('Set up main dependencies'){
                steps{
                    sh "sudo apt update"
                    sh "sudo apt-get install python3 python3-pip python3-venv -y"
                }
            }
            stage('Initate virtual environment'){
                steps{
                    sh "python3 -m venv venv"
                    sh "source venv/bin/activate"
                }
            }
            stage('Install modules'){
                steps{
                    sh "pip3 install -r requirements.txt"
                }
            }
            stage('Run ansible'){
                steps{
                    sh "ansible-playbook -i inventory.yaml playbook.yaml"
                }
            }
        }
}