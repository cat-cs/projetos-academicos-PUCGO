# Protótipo de Automação Residencial com Arduino

Este projeto apresenta um protótipo de automação residencial utilizando a plataforma Arduino. O objetivo é monitorar e controlar variáveis ambientais, como temperatura, umidade e luminosidade, proporcionando maior conforto e eficiência energética. O protótipo foi construído usando o simulador do ThinkerCad, para o módulo em Java foram adotadas medidas fictícias com biblioteca Radom.

## Componentes Utilizados

- **Arduino UNO**: Microcontrolador principal para integração dos sensores e comunicação com o sistema.
- **Sensor de Temperatura e Umidade (TMP36)**: Responsável pela leitura da temperatura e umidade do ambiente.
- **Sensor de Luminosidade (LDR)**: Captura a intensidade luminosa do ambiente.
- **Potenciômetro**: Por limitações do ThinkerCad, foi utilizado um potenciômetro para simular a entrada de dados para Sensor de Umidade do Ar.

## Esquema do Circuito

O esquema detalhado das conexões dos componentes pode ser visualizado no seguinte link:

Protótipo no Tinkercad [aqui](https://www.tinkercad.com/things/5AK6jcR6vqw-pi-v-b/editel?returnTo=https%3A%2F%2Fwww.tinkercad.com%2Fdashboard&sharecode=YIDjlA0aCebJf5z-QL2UP-Uz5tEqp-A0Xtxn0CP0n8E)


## Código Fonte

O código fonte utilizado para a programação do Arduino está disponível no arquivo `arduino.java` neste repositório.

## Interface Gráfica

Para a visualização dos dados coletados e controle dos dispositivos, foi desenvolvida uma interface gráfica no Figma, acessível pelo link:

Protótipo no Figma [aqui](https://www.figma.com/proto/GkHVVXgmkJFAWKhUXjD0cS/PI-V-B?node-id=0-1&t=ZMu8a4Aygakyaufz-1)

## Diagrama UML

O diagrama de classes UML, representando a arquitetura do sistema, está disponível na pasta `UML` deste repositório.

## Como Executar o Projeto

1. **Montagem do Circuito**: Conecte os sensores ao Arduino conforme o esquema fornecido.
2. **Upload do Código**: Utilize a IDE do Arduino para carregar o código fonte na placa.
3. **Configuração da Interface**: Acesse a interface gráfica através do link fornecido e conecte-a ao módulo Bluetooth para iniciar o monitoramento.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

