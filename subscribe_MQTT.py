from mqtt_class import MQTT_Client

broker = 'localhost'
port = 7777
topic = "mensagem"

if __name__ == '__main__':

	client = MQTT_Client(broker = broker, port = port, topic = topic)
	client.subscribe()