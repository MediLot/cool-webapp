# COOL for COVID19 Demo App

This document is for the COVID19 Demo App which is based on the cohana system. 

For more information, you can refer to the [paper](https://www.comp.nus.edu.sg/~ooibc/icde20cool.pdf).

## Set up

Please pre-install the docker environment at first.

```sh
sh start.sh
```

`start.sh` will build and run the needed docker containers
```sh
# check docker container status
docker ps -a

# stop the demo dockers
docker stop <container-id>
```

go to `http://127.0.0.1:8201/`

### Dataset Required documents:

1. Dataset should be a csv file with "," delimiter (normally dumped from a database
table). 

2. It would be better to use the app if the dataset includes `id`, `time`, `event` columns.

3. The elements in the `event` column should be same as the columns of the dataset. 

4. The `time` column should follow "YYYY-MM-DD" format. 

5. Example file can be found [here](example-data/example.csv).

### Login

User ID: root
Password: zaq12wsx


### Scripts:

1. [init.sh](init.sh): load the demo dataset and start two dockers.
	It uses [preprocess.py](utils/preprocess.py) to load the demo dataset and run init.sh.

2. [start.sh](start.sh): build the dockers for scape and scape-front-end, and start them in background.

3. [stop.sh](stop.sh): stop the dockers which contain scape and scape-front-end.

4. [restart.sh](restart.sh): stop and restart the dockers.

5. [docker.sh](docker.sh): example script for installing docker in AWS EC2.

6. [clean.sh](clean.sh): remove all docker containers and all docker images about scape.
