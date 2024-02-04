# Commands

List of commands used

## Often used

```
docker ps -a								list all containers
docker start (container)					start container
docker stop (container)						stop container
docker rm (container)						remove container
docker images								show all images
docker rmi (image)							remove image
```



## Installing MQTT server using Docker

#### Create and run a new container from an image

Command:

```
docker run -it -d --name mosquitto -p 1883:1883 -p 9001:9001 -v 		/home/mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```

Options:

	-d							detach (run container in background)
	--name mosquitto 			give name "mosquitto" to the new container
	-p 1883:1883 / 9001:9001	map ports to the container (host:container)
	-v 							mount a volume (host-path:container-path)
	eclipse-mosquitto			the image we use

#### We want the container to always be on

Command:

```
docker update --restart=always mosquitto
```

Options:

```
update					update the container configuration
--restart=always		if the container exits for any reason, it gets restarted
mosquitto				the container name
```





## Backend 

```
pip install pipreqs							used to create requirements.txt for only project	(updated verison manually)
docker build -t backend .					create image for backend
	-t backend								give name to image
```

Create container from image:

```
docker run --name backend -p 8000:8000 -v /home/pi/esp-camera/Server/uploads:/app/uploads backend
	--name backend					give name to container
	-p 8000:8000					map port
	-v								map host-directory to container-directory
	backend							image-name
```





## Docker compose

```
docker compose build
docker compose up
docker compose down
docker compose stop
```











