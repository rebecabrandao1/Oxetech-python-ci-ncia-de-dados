# Datalogger Arduino e Python

Este é um projeto simples de datalogger utilizando Arduino e Python para gravar dados de umidade e temperatura em um arquivo CSV.

## Requisitos

- Arduino Uno
- Sensor de Umidade e Temperatura DHT11
- Computador com Python 3 e PySerial instalado
- Para instalar a biblioteca do PySerial é só digitar no terminal: `pip install pyserial`
- Para baixar a biblioteca do DHT11 acesse esse [link](https://github.com/dhrubasaha08/DHT11), baixe e em seguida clique em sketch > include libraries > add .ZIP library


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

## Uso com Google Colab

1. Faça upload do arquivo `datalogger.csv` gerado pelo Arduino para o Google Colab.
2. Crie um novo notebook Python no Google Colab.
3. Utilize o seguinte código para carregar e visualizar os dados do arquivo CSV:

```python
import pandas as pd

# Carregar arquivo CSV
df = pd.read_csv('caminho_para_o_arquivo_datalogger.csv')

# Exibir as primeiras linhas do dataframe
print(df.head())
````
## Contribuição

Contribuições são bem-vindas! Para maiores informações, por favor, abra uma issue para discutir o que você gostaria de mudar ou faça um clone do repositório.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
