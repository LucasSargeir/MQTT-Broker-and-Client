# Broker MQTT e Clientes Publish e Subscribe

Implementação de clientes MQTT publish e subscribe, e um Broker para troca de mensagens. A prosposta foi implementar o o serviço para troca de mensagens de forma persistente.

**Tecnologias:**

- Python (3.8).



**Dependências:**

- hbmqtt;
- paho-mqtt;
- asyncio;
- logging;
- radom;
- time.



## Módulos

- <u>Broker</u> 

  Para criação do Broker foram utilizados os módulos `hbmqtt`, `asyncio` e `logging`.  O módulo `hbmqtt` é um módulo que permite criar nossos próprios Brokers através do MQTT Mosquitto, esse módulo também nos permite instanciar as configurações dos nossos Brokers através de um objeto Python. Por trabalhar com rotinas assíncronas foi necessário a utilização do módulo `asyncio`.

  O módulo `logging` foi utilizado para gerar o Log do nosso Broker, assim podemos saber sempre que um novo cliente for conectado.

  

- <u>Classe MQTT_Client</u>

  A classe MQTT_Client foi criada com o objetivo de facilitar a criação e conexão de novos clientes. 

  **Construtor**

  O construtor da classe serve para fazer a conexão com um broker em um determinado tópico. Todos os parâmetros são opicionais, e se não forem passados, seguirão com os valores apresentados abaixo:

  - `port = 7777`
  - `topic = 'deafult-  topic'`
  - `broker = '127.0.0.1'`
  - `client_id = None`
  - `user = None`
  - `password = None`

  

  **Métodos**

  Uma vez que o objeto é instanciado ele tem acesso a dois métodos: `publish` e `subscribe`.

  O método `subscribe` serve para se inscrever em um tópico, ou seja, toda vez que o tópico receber uma mensagem você receberá essa mensagem.

  O método `publish` serve para se tornar um publicador, ou seja, você poderá enviar mensagens ao tópico conectado. Esse método pode receber um parâmetro opcional `time_sleep` que tem por padrão o valor 1. Esse parâmetro representa o tempo de espera entre uma mensagem e outra.



- <u>Clientes Publisher e Subscriber</u>

  Os clientes publish e subscribe intanciam um objeto da classe MQTT_Client e chamam seus respectivos métodos.

  

## Execução 

Para executar cada módulo do sistema siga as instruções abaixo:

- Broker:

  ```bash
  python broker.py
  ```

- Clientes:

  ```bash
  # Publisher
  python publish_MQTT.py
  
  # Subscriber
  python subscribe_MQTT.py
  ```

