docker stop $(docker ps -q --filter ancestor=med-front )
docker stop $(docker ps -q --filter ancestor=med )

