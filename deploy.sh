#!/bin/sh
docker compose down
docker image rm fast-aws-apigateway
docker build -t fast-aws-apigateway .
docker compose up -d