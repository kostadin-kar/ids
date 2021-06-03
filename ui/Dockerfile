FROM node:16-alpine
WORKDIR /app/ui
COPY ./ui/package.json ./ui/package-lock.json ./
RUN npm install
COPY ./ui .
EXPOSE 4200
RUN npm run build