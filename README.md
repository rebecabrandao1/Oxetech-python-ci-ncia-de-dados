# Datalogger Arduino e Python

Este é um projeto simples de datalogger utilizando Arduino e Python para gravar dados de umidade e temperatura em um arquivo CSV.

## Requisitos

- Arduino Uno
- Sensor de Umidade e Temperatura DHT11
- Computador com Python 3 e PySerial instalado

## Instalação

1. Faça o upload do código `arduino_datalogger.ino` para o seu Arduino Uno.
2. Conecte o sensor DHT11 ao Arduino conforme o esquema de conexão.

## Uso

1. Execute o script `datalogger.py` no seu computador.
2. Pressione Enter no terminal para iniciar a leitura dos dados da porta serial.
3. Pressione Enter novamente para parar a leitura e fechar o arquivo CSV.

## Esquema de Conexão

| Sensor DHT11 | Arduino Uno |
|--------------|-------------|
| VCC          | 5V          |
| DATA         | 7           |
| GND          | GND         |

## Contribuição

Contribuições são bem-vindas! Para maiores informações, por favor, abra uma issue para discutir o que você gostaria de mudar ou faça um clone do repositório.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
