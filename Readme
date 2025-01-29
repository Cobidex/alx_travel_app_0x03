# alx_travel_app_0x03

## Background Task Management with Celery and Email Notifications

### Setup
1. Install dependencies: `pip install celery`
2. Start RabbitMQ: `sudo systemctl start rabbitmq-server`
3. Run Celery: `celery -A alx_travel_app worker --loglevel=info`
4. Make a booking via API, and Celery will handle email sending asynchronously.

### Configuration
- Celery broker: `amqp://localhost`
- Email backend: Django's built-in email backend
