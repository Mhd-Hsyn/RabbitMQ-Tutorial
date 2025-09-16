# 🐇 RabbitMQ Roadmap (Beginner → Advanced)

## Stage 1 — Basics (Hello RabbitMQ)

### 🔑 Concepts to learn
- What is a Message Broker? **Queue vs Pub/Sub**.
- Core RabbitMQ terms: **Producer, Consumer, Queue, Exchange, Binding, Routing Key, vHost**.
- Exchange types: **Direct, Fanout, Topic, Headers**.

### 🎯 Hands-on
- Install RabbitMQ (**Docker recommended**).
- Write a simple **Producer** that sends a message and a **Consumer** that receives it.
- Try with Python library → **pika**.

### 📦 Deliverable
- Simple project with **producer.py** and **consumer.py** sending/receiving JSON message.


## Stage 2 — Exchanges & Routing

### 🔑 Concepts to learn
- **Direct exchange** → Route message to specific queue with exact routing key.
- **Fanout exchange** → Broadcast to all queues.
- **Topic exchange** → Wildcard routing (e.g. `order.*`, `*.created`).
- **Headers exchange** → Match based on message headers instead of routing key.

### 🎯 Hands-on
- Create **3 consumers** bound to different queues.
- Publish messages with different routing keys.
- Observe how routing decides where messages go.

### 📦 Deliverable
- Demo repo with multiple consumers showing Direct/Fanout/Topic routing.


## Stage 3 — Message Acknowledgment & Reliability

### 🔑 Concepts to learn
- **ACK, NACK, Reject**.
- **Auto-ack vs Manual ack**.
- **Message durability** (persistent queues & messages).
- **Publisher confirms** (ensures message actually stored).
- **Dead Letter Exchange (DLX)** for failed messages.

### 🎯 Hands-on
- Write consumer with manual `basic_ack()`.
- Simulate failure → send to **DLX queue**.
- Enable **Publisher Confirms** for reliable delivery.

### 📦 Deliverable
- Order service → publishes **`order.created`**.
- Consumer → processes and NACK sends failed msgs to DLX.


## Stage 4 — Work Queues & Scaling Consumers

### 🔑 Concepts to learn
- **Competing consumers** (multiple consumers on same queue).
- **Fair dispatch** with prefetch count.
- **Load balancing** with round-robin dispatch.

### 🎯 Hands-on
- Run **2–3 consumers** on the same queue.
- Test **work distribution**.
- Use `basic_qos(prefetch_count=1)` for fair load distribution.

### 📦 Deliverable
- Worker pool processing jobs from a shared queue.


## Stage 5 — Integrating with Django/DRF

### 🔑 Concepts to learn
- Use **Celery** with RabbitMQ as broker.
- **Async task processing** (send email, background jobs).
- Retry, scheduling, and task chaining.

### 🎯 Hands-on
- Setup **Django + Celery + RabbitMQ**.
- Create async tasks (send email, generate report, payment confirmation).
- Test **retry/backoff** on failure.

### 📦 Deliverable
- Django project with Celery tasks using RabbitMQ as broker.


## Stage 6 — Advanced Features

### 🔑 Concepts to learn
- **Priority Queues** (process high-priority messages first).
- **Delayed Messaging** (using plugins / TTL + DLX pattern).
- **Message TTL** (expire old messages).
- **Alternate Exchanges** (fallback when no queue matches).

### 🎯 Hands-on
- Setup **priority queue** (VIP orders before normal orders).
- Setup **TTL** so expired messages go to dead-letter.
- Setup **delayed retry** with exponential backoff.

### 📦 Deliverable
- Retry system → failed payment retries after **5s, 10s, 30s**.


## Stage 7 — Monitoring & Observability

### 🔑 Concepts to learn
- RabbitMQ **Management Plugin** (queues, exchanges, messages, consumers).
- Monitoring with **Prometheus + Grafana**.
- Logs, metrics: **queue depth, message rate, unacked messages**.

### 🎯 Hands-on
- Enable RabbitMQ management dashboard → **http://localhost:15672**.
- Add **Prometheus exporter** + visualize metrics in Grafana.

### 📦 Deliverable
- Monitoring dashboard showing **queue length & consumer lag**.


## Stage 8 — Security & Production Setup

### 🔑 Concepts to learn
- **Authentication & Authorization** in RabbitMQ.
- **vHosts** for multi-tenant isolation.
- **TLS** for encrypted connections.
- **HA with RabbitMQ cluster** (mirrored queues).

### 🎯 Hands-on
- Setup multiple vHosts (`/orders`, `/users`).
- Configure **TLS**.
- Simulate **cluster** with Docker Compose (3-node RabbitMQ).

### 📦 Deliverable
- RabbitMQ cluster config + TLS enabled connection.


## Stage 9 — Advanced Messaging Patterns

### 🔑 Concepts to learn
- **RPC over RabbitMQ** (request/response pattern).
- **Event-driven architecture** with RabbitMQ.
- **Saga pattern** with RabbitMQ as event bus.
- **Event sourcing** (store events, replay them).

### 🎯 Hands-on
- Implement **RPC**: Order service requests Payment service → gets response.
- Implement **event-driven order flow**: `OrderCreated` → Payment, Inventory, Notification all consume.
- Implement **saga rollback** if payment fails.

### 📦 Deliverable
- Mini **E-commerce** system (Order, Payment, Inventory, Notification services connected via RabbitMQ).


## Stage 10 — Alternatives & Migration

### 🔑 Concepts to learn
- When to use **RabbitMQ vs Kafka**.
- **RabbitMQ** → good for tasks, short-lived messages, small scale async jobs.
- **Kafka** → better for streams, event sourcing, replay, analytics, high throughput.
- **Hybrid architecture** (RabbitMQ for tasks, Kafka for event streams).

### 📦 Deliverable
- Comparison doc + hybrid demo (Django async tasks in RabbitMQ + Kafka for event storage).


---

## 🏁 Final Checklist (RabbitMQ Mastery)

✅ Know all **exchange types** (Direct, Fanout, Topic, Headers)  
✅ **Durable queues**, persistent messages, publisher confirms  
✅ **Manual ack/nack**, DLX, retries  
✅ **Celery integration** with Django  
✅ **Priority queues**, TTL, delayed retries  
✅ Monitoring with **Prometheus + Grafana**  
✅ Secure & cluster RabbitMQ  
✅ Implement **RPC, Saga**, event-driven microservices  
✅ Clear when to use **RabbitMQ vs Kafka**
