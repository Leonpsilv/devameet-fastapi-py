# Devameet API FastAPI - Python

## Descrição
Projeto desenvolvido em Python, com o intuito de aprender sobre o FastAPI.
O projeto é um inspirado no [Google Meet](https://meet.google.com
) e no [Gather](https://www.gather.town) e pode ser visualizado no [Figma](https://www.figma.com/file/mIXcu8SJWqi0ylVHtZn89a/Devameet-(Projeto-2023)).
 
## Tecnologias
* fastapi 0.95.2
* bcrypt 4.0.1
* python-jose 3.3.0
* SQLAlchemy 2.0.15
* pydantic 0.22.0
* postgreSQL
* docker-compose
* docker 

### Configuração do ambiente de desenvolvimento

1. clonar o repositório `git clone https://github.com/Leonpsilv/devameet-fastapi-py.git` 
1. fazer uma copia do arquivo `.env.example` e renomear o novo arquivo de `.env`
1. configurar as variáveis de ambiente no arquivo `.env`
1. configurar o ambiente virtual para instalar as dependências do projeto
1. instalar as dependencias do projeto `pip install`, presentes no arquivo _requirements.txt_
1. criar um container com o docker executando o comando `docker compose up -d`
1. executar o comando `uvicorn src.main:app --reload` para subir a aplicação em ambiente de desenvolvimento

### Autor
- Leonardo Pinheiro da Silva