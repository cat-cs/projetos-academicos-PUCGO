### PROJETO INTEGRADOR I – A
# ChatBot Clínica Médica

## Descrição

Este projeto implementa um chatbot simples, chamado Célia, que simula um atendente virtual para uma clínica médica. O chatbot tem como objetivo auxiliar os pacientes com agendamentos, informações sobre os serviços oferecidos pela clínica, e permitir que o paciente fale com um atendente humano. O sistema interage com o usuário através de um menu interativo, onde o usuário pode escolher entre diferentes opções para obter as informações desejadas ou realizar ações como agendar ou cancelar consultas.

## Funcionalidades

- **Atendimento inicial**: O chatbot apresenta um menu de boas-vindas com as opções de agendamento, informações sobre serviços ou falar com um atendente.
- **Agendamento de consultas**: Permite ao usuário agendar uma consulta, escolher uma especialidade e fornecer o nome do paciente para confirmar a marcação. Também é possível cancelar uma consulta.
- **Informações sobre serviços**: O chatbot oferece detalhes sobre os serviços da clínica, como preços de consultas médicas, exames laboratoriais e vacinas disponíveis.
- **Falar com um atendente**: O chatbot conecta o usuário com um atendente humano, permitindo que ele aguarde na fila até que um atendente esteja disponível.
- **Finalização do atendimento**: O usuário pode encerrar o atendimento a qualquer momento, agradecendo pela assistência e se despedindo.

## Requisitos

- **Java 8 ou superior**: O projeto foi desenvolvido em Java e requer a versão 8 ou superior do JDK para compilação e execução.
- **Scanner**: A classe `Scanner` é utilizada para capturar a entrada do usuário no terminal.

## Como Executar

1. **Instalar o Java**: Se você ainda não tem o Java instalado, baixe e instale a versão mais recente do JDK (Java Development Kit) no [site oficial do Java](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
2. **Compilar o código**: Compile o código-fonte com o seguinte comando:
   ```bash
   javac ChatBot.java
    ```
### Executar o Chatbot
Após a compilação, execute o chatbot com o comando:
  ```bash
   java ChatBot
  ```
### Como Funciona

#### Menu Principal

Ao iniciar o programa, o usuário verá um menu com as seguintes opções:

- **Agendamentos e Consultas**
- **Informações sobre serviços**
- **Falar com um atendente**
- **Encerrar atendimento**

#### Submenus

**Agendamentos e Consultas**  
O usuário pode escolher entre:

- **Agendar uma consulta**: O usuário escolhe uma especialidade médica e fornece o nome do paciente para agendar a consulta.
- **Cancelar uma consulta**: O usuário informa o nome do paciente para cancelar a consulta previamente agendada.

**Informações sobre serviços**  
O usuário pode obter informações sobre:

- **Consultas médicas**: Preços das consultas para diferentes especialidades.
- **Exames laboratoriais**: Preços e tipos de exames disponíveis.
- **Vacinas**: Informações sobre vacinas, incluindo a vacina contra COVID-19, MMR e HPV.

**Falar com um atendente**  
O usuário pode aguardar na fila para ser atendido por um humano.

**Encerramento**  
O usuário pode encerrar o atendimento a qualquer momento selecionando a opção 0.

### Estrutura do Código

- **Menu principal**: O código apresenta ao usuário um menu principal com opções de agendamento, informações e suporte.
- **Menus secundários**: Dependendo da escolha do usuário, são apresentados menus específicos para agendar consultas, obter informações ou falar com um atendente.
- **Controle de fluxo**: O código usa estruturas `switch` para navegar entre as diferentes opções do menu e realizar as ações solicitadas.

### Considerações Finais

Este chatbot é um protótipo simples que simula o atendimento de uma clínica médica. Ele pode ser expandido com novas funcionalidades, como integração com sistemas de agendamento reais, uma interface gráfica ou mais opções de interações para enriquecer a experiência do usuário.

Se tiver dúvidas ou sugestões de melhorias, fique à vontade para contribuir!

### Licença

Este projeto é de código aberto e pode ser usado, modificado e distribuído livremente, desde que os devidos créditos sejam dados ao autor original.


