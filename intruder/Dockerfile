FROM python:3.8-alpine
WORKDIR /app
ENV FLASK_APP=requester
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers make g++
WORKDIR /app/intruder
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./intruder/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./intruder ./
EXPOSE 5002
CMD ["flask", "run", "--host", "0.0.0.0"]