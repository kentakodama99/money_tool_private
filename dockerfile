FROM node:latest

WORKDIR /app/vue

RUN apt-get install -y gnupg
RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs 
RUN npm install -g @vue/cli