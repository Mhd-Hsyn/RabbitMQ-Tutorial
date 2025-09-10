import pika
from config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD
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

# Queue declare (idempotent – agar pehle se hai to reuse karega)
channel.queue_declare(queue='hello')

# Message bhejna
channel.basic_publish(
    exchange='',      # default exchange
    routing_key='hello',  # queue name
    body='Hello RabbitMQ!'
)

print(" [x] Sent 'Hello RabbitMQ!'")
connection.close()
