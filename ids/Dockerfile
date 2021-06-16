FROM frolvlad/alpine-python-machinelearning
WORKDIR /app
ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers make g++ python3-dev
WORKDIR /app/ids
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./ids/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./ids ./
RUN python -m grpc_tools.protoc -I ./ --python_out=. --grpc_python_out=. ./server.proto
EXPOSE 5001
EXPOSE 50051
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]