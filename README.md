# ESP-Camera for Missing-Semester

### Team members:

| Name                    | Student-ID |
| ----------------------- | ---------- |
| Daniela Eberhard        | 12006661   |
| Sebastian Hollersbacher | 12015864   |





## Goal

The goal of this project is to get a better understand in these areas:

- Server-Hosting
- Docker
- Backend - Frontend
- Garmin Apps
- ESP32-Cam modules





## The way the project works

The camera (ESP32-Cam) takes a picture upon request and uploads it to the server using a http-Post request.

A request can be made using mqtt-publish with the hosted mqtt-broker on the server.

The backend is a flask-app where pictures can be uploaded (Post), listed and downloaded (Get).

The frontend is a react-app showing images from the backend. It can also publish mqtt messages

The Garmin app can request images from the backend and show them on the smart-watch display





## Project Structure

The project consist of 4 different parts:

- Server (Hosted on Raspberry Pi 4 Model B)
- Camera (esp32-cam modules)
- Trigger (ESP01 Wi-Fi-modules)
- Watch (Garmin Smartwatch)

![ProjectStructure](./Documentation/ProjectStructure.png)



Request are sent to the camera via MQTT hosted on the server. 

The camera is then taking a picture and sending it to the server as a HTTP POST request.

From there, the images can be viewed using the frontend webpage or the smartwatch app.



#### Server Structure

The server is using Docker to host the different applications.

![ServerStructure](./Documentation/ServerStructure.png)





## Future Improvements

- Fixing upload of images (does not work sometimes)
- Better communication between frontend and backend
- Improving the design of the frontend
- Port-forwarding (Currently works only in local network)