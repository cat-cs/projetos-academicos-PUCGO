# Lista de Contatos

Este é um sistema simples para gerenciamento de contatos utilizando MySQL como banco de dados e Python para a implementação da lógica.

## Funcionalidades

- **Adicionar contato**: Permite adicionar um novo contato, incluindo nome, telefone e e-mail.
- **Visualizar contatos**: Exibe a lista de contatos com informações de nome, telefones e e-mails em formato de tabela.
- **Alterar dados de contato**: Permite atualizar os dados de um contato existente, como nome, telefone e e-mail.
- **Excluir contato**: Permite excluir um contato da lista.

## Requisitos

- Python 3.x
- MySQL
- Bibliotecas Python:
  - `mysql-connector`
  - `tabulate`

### Como Instalar as Dependências

1. Instale o Python 3.x se ainda não o tiver.
2. Instale as bibliotecas necessárias executando o comando:
    ```bash
    pip install mysql-connector tabulate
    ```
### Como Usar o Sistema

1. Clone o repositório ou faça o download do código-fonte.
2. Execute o script Python:
    ```bash
    python lista_contatos.py
    ```

3. O programa exibirá um menu no terminal onde você pode escolher as opções de adicionar, visualizar, atualizar ou excluir contatos.

### Detalhes Técnicos

- O banco de dados é estruturado com três tabelas: `contatos`, `telefones` e `emails`.
- O sistema permite associar múltiplos telefones e e-mails a um único contato através de chaves estrangeiras (`id_contatos`).
- O código é escrito em Python e utiliza a biblioteca `mysql-connector` para interagir com o banco de dados MySQL.
- A interface é de linha de comando (CLI), com interação por meio de inputs no terminal.

### Contribuição

Sinta-se à vontade para contribuir com melhorias no projeto, sugestões de novos recursos ou correções de bugs.

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature-nome`).
3. Commit suas alterações (`git commit -m 'Adicionando nova funcionalidade'`).
4. Faça o push para a branch (`git push origin feature-nome`).
5. Abra um Pull Request.

### Licença

Este projeto é de código aberto, licenciado sob a [MIT License](LICENSE).
