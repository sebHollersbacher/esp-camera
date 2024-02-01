FROM node:latest

WORKDIR /react-app

COPY public /react-app/public
COPY src /react-app/src
COPY package.json /react-app
COPY tsconfig.json /react-app

RUN npm install --legacy-peer-deps

CMD ["npm", "start"]