docker stop $(docker ps -q --filter ancestor=med-front )
docker stop $(docker ps -q --filter ancestor=med )
docker build -t med cool
docker build -t med-front .
docker run -d -v $(pwd)/cohana:/cohana -p 8200:9998 med
docker run -d -v $(pwd):/cohana -p 8201:9999 --link $(docker ps -q --filter ancestor=med ):med med-front
