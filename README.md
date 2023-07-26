# Contatos API

Exemplo de API de contatos que permite realizar operações CRUD (Create, Read, Update, Delete) em uma lista de contatos pré setada.

## Configuração do ambiente de desenvolvimento

1. Instale o Python 3.10 ou superior e o pip (gerenciador de pacotes Python) em sua máquina.
     
2. Crie um ambiente virtual (venv) para isolar as dependências deste projeto:
    python -m venv venv

3. Ative o ambiente virtual:
    venv\Scripts\activate

Considere atualizar seu pip do venv:
    pip install --upgrade pip

4. Instale as dependências do projeto:

    pip install -r requirements.txt

## Configuração do banco de dados

1. Edite o arquivo `database.py` na pasta `database` e configure as informações do seu banco de dados (host, usuário, senha, nome do banco de dados).

## Executando a API

Para executar a API localmente, vá para a pasta `app` e execute o arquivo `app.py`:
    cd app</br>
    python app.py

Isso iniciará o servidor de desenvolvimento na porta 5000.

## Testando a API(por questoes de otimização projetei em outro local e iniciada de forma assincrona com a API, desta forma os testes serão bem executados)

Os testes automatizados podem ser executados usando o módulo `unittest`. Vá para a pasta `tests` e execute o arquivo `test.py`:
    cd tests</br>
    python test.py

Isso executará os testes e mostrará o resultado no terminal.


### Conclusão

Agora você pode acessar a API através de um cliente REST, como o Postman, usando as rotas definidas na API.
