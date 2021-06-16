FROM node:16-alpine
WORKDIR /app/ui
RUN apk add --update --no-cache python3 make gcc g++
COPY ./ui/ui/package.json ./ui/ui/package-lock.json ./
RUN npm install
COPY ./ui/ui .
EXPOSE 4200 5000 5001 5002
RUN npm run build