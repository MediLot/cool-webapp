docker build -t med scape
docker build -t med-front .
docker run -d -v $(pwd)/cohana:/cohana -p 8200:9998 med
docker run -d -v $(pwd):/cohana -p 8201:9999 --link $(docker ps -q --filter ancestor=med ):med med-front
# sh start_django.sh
