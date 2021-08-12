ls
sudo scp /home/jenkins/Project2/docker-compose.yaml jenkins@swarm-manager:/home/jenkins

ssh swarm-manager << EOF
export DATABSE_URI=$DATABASE_URI
docker stack deploy --compose-file docker-compose.yaml BATTLE_SIM
EOF