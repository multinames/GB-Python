import pika

credentials = pika.PlainCredentials('test_user', 'ghbdtn00')
parameters = pika.ConnectionParameters('192.168.136.128', 5672, 'test_host', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='test_host')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

connection.close()

print("Your message has been sent to the queue.")