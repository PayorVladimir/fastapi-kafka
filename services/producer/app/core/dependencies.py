from aiokafka import AIOKafkaProducer

kafka = None


def get_queue() -> AIOKafkaProducer:
    assert kafka, "Kafka producer has not been initialized"
    return kafka
