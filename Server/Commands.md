# Commands



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

