# FastAPI-Kafka geo streaming

## How to run?
`docker compose up -d`

## Kafka
Kafka will be available at `localhost:9092`


## Producer app
Write messages to a topic at `localhost:8001/producer/<topicname>`

## Consumer app
Read topic messages at `localhost:8002/consumers/<topic_name>`
