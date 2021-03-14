from paho.mqtt import client as mqtt_client
import random
import time

class MQTT_Client:
	
	# - OPÇÃO DE BROKER WEB GRÁTIS
	# broker = 'broker.emqx.io'
	# port = 1883	
	# topic = "/python/mqtt"

	def __init__(self, port = 7777, topic = 'deafult-topic', broker = '127.0.0.1', client_id = None, user = None, password = None):
		def on_connect(client, userdata, flags, rc):	
			if rc == 0:
				print(f'[STATUS-{rc}] Conectado ao MQTT Broker!\n')
			else:
				print(f'[STATUS-{rc}] A conexão falhou!\n')

		def on_disconnect(client, userdata, rc):
			print("A conexão foi interrompida, tentando reconectar...")
			if rc == 0:
				print(f'[STATUS-{rc}] Desconectado\n')

		self.port = port
		self.topic = topic
		self.broker = broker

		if client_id != None:
			self.client_id = client_id
		else:
			self.client_id = f'User-{random.randint(0, 1000)}'
		
		self.client = mqtt_client.Client(self.client_id, clean_session = False)
		self.client.on_connect = on_connect
		self.client.on_disconnect = on_disconnect

		if user != None and password != None:
			self.client.username_pw_set(user, password)
		
		print("Conectando...")
		self.client.connect(self.broker, self.port)



	def publish(self, time_sleep = 1):
		print(f"Tópico da conexão: {self.topic}")
		self.client.loop_start()
		msg_count = 0
		while True:
			time.sleep(time_sleep)
			msg = input(f"Nova mensagem\n[{self.client_id}]: ")
			msg = f"[{self.client_id}]: {msg}"
			result = self.client.publish(self.topic, msg)
			status = result[0]
			if status == 0:
				print(f'Enviando...\n')
			else:
				print(f'Falha ao enviar mensagem ao tópico {self.topic}')
			msg_count += 1



	def subscribe(self):
		def on_message(client, userdata, msg):
			print(msg.payload.decode())

		print(f"Tópico da conexão: {self.topic}")
		self.client.subscribe(self.topic)
		self.client.on_message = on_message

		self.client.loop_forever()
