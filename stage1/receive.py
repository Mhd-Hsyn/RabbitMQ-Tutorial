import pika
from config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
)

credentials = pika.PlainCredentials(
    username= RABBITMQ_USER,
    password= RABBITMQ_PASSWORD
)

connection_parameter = pika.ConnectionParameters(
    host= RABBITMQ_HOST,
    port= RABBITMQ_PORT,
    credentials=credentials
)

# RabbitMQ se connect karo
connection = pika.BlockingConnection(
    parameters= connection_parameter
)
channel = connection.channel()

# Same queue declare (idempotent)
channel.queue_declare(queue='hello')

# Callback jab message receive ho
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Consumer setup
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
