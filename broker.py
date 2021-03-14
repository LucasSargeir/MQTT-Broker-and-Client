# from hbmqtt.client import MQTTClient, ClientException
# from hbmqtt.mqtt.constants import QOS_1
from hbmqtt.broker import Broker
import logging
import asyncio

logger = logging.getLogger(__name__)

config = {
	'listeners': {
		'default': {
			'type': 'tcp',
			'bind': '127.0.0.1:7777',
			'max_connections': 500,
		},
		
	},
	'sys_interval': 10,
	'auth': {
		'allow-anonymous': True,
		'plugins': [
			'auth_file', 'auth_anonymous'
		]

	},
	'topic-check': {
		'enabled': True,
		'plugins': [
			'topic_taboo'
		]
	}
}

# - METODO PARA INTECEPTAR AS MENSAGENS DO BROKER
# async def brokerGetMessage():
# 	C = MQTTClient()
# 	await C.connect('mqtt://127.0.0.1:7777/')
# 	await C.subscribe([
# 		("mensagem", QOS_1)
# 	])
# 	logger.info('Subscribed!')
# 	try:
# 		for i in range(1,100):
# 			message = await C.deliver_message()
# 			packet = message.publish_packet
# 			print(packet.payload.data.decode('utf-8'))
# 	except ClientException as ce:
# 		logger.error("Client exception : %s" % ce)

async def broker_start():
	broker = Broker(config)
	await broker.start()


if __name__ == '__main__':
	formatter = "[%(asctime)s] :: %(levelname)s  :: %(name)s\t:: %(message)s"
	logging.basicConfig(level = logging.INFO, format = formatter)

	try:
		asyncio.get_event_loop().run_until_complete(broker_start())
		# asyncio.get_event_loop().run_until_complete(brokerGetMessage())
		asyncio.get_event_loop().run_forever()
	except KeyboardInterrupt:
		asyncio.get_event_loop().run_until_complete(broker.shutdown())
	finally:
		asyncio.get_event_loop().close()