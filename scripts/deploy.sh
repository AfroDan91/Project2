
rsync docker-compose.yaml swarm-manager:

ssh swarm-manager << EOF
export DATABSE_URI=$DATABASE_URI
docker stack deploy --compose-file docker-compose.yaml BATTLE_SIM
EOF