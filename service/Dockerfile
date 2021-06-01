FROM python:3.8-alpine
WORKDIR /app
ENV FLASK_APP=storyController
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers make g++
WORKDIR /app/service
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
#RUN pip install --no-cache-dir --force-reinstall -Iv grpcio==1.36.1
COPY ./service/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
COPY ./ids/server.proto ./service/server.proto
WORKDIR /app/service
RUN python -m grpc_tools.protoc -I ./ --python_out=. --grpc_python_out=. ./server.proto
COPY ./service ./
EXPOSE 5001
EXPOSE 50051
CMD ["flask", "run", "--host", "0.0.0.0"]