FROM python:3.8-alpine
WORKDIR /app
ENV FLASK_APP=storyController
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ./ --python_out=. --grpc_python_out=. ./server.proto
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]