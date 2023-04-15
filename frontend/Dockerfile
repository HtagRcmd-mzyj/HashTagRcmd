FROM node:alpine
WORKDIR /docker-server/frontend

#COPY package.json package-lock.json ./
COPY package.json ./

RUN npm install
RUN npm install axios
RUN npm install styled-components

#RUN npm install react-scripts@3.4.1 -g
COPY ./ ./

EXPOSE 3000
CMD ["npm", "start"]
