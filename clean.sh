docker rm $(docker ps -q --filter ancestor=scape)
docker rmi $(docker images -a -q --filter ancestor=scape)
docker rm $(docker ps -q --filter ancestor=scape-front )
docker rmi $(docker images -a -q --filter ancestor=scape-front )