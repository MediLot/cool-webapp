docker rm $(docker ps -q --filter ancestor=cool)
docker rmi $(docker images -a -q --filter ancestor=cool)
docker rm $(docker ps -q --filter ancestor=cool-front )
docker rmi $(docker images -a -q --filter ancestor=cool-front )