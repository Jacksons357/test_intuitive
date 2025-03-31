# Teste - IntuitiveCare

Este é um projeto de teste para a empresa IntuitiveCare.

Siga corretamente as instruções deste README para garantir uma instalação e configuração sem problemas.

## Requisitos

Antes de começar, verifique se você tem as seguintes ferramentas instaladas:

- **Python 3.11+** - Para rodar a aplicação Python
- **Node.js** - Para executar o ambiente de desenvolvimento frontend (caso necessário)
- **MySQL** - Banco de dados utilizado pelo projeto
- **Docker** - Para criar e rodar o contêiner da aplicação
- **Docker Compose** - Geralmente incluído no Docker Desktop
- **Git** - Para clonar o repositório

### Para verificar se essas ferramentas estão instaladas:

```bash
python --version
node --version
mysql --version
docker --version
docker compose version
```

**Docker Compose**: Geralmente já incluído no Docker Desktop.
**Git (opcional)**: Para clonar o repositório do projeto.

## Configuração do Projeto

### 1. **Clone o repositório**

```bash
git clone https://github.com/Jacksons357/test_intuitive.git
cd test_intuitive
```

1.1. Abra em seu editor(VSCode)

```bash
code .
```

### 2. **Configure as variáveis de ambiente**

2.1. Abra o terminal e acesse a pasta backend:

```bash
cd backend/
```

2.2. Copie o arquivo `.env.example` e crie o arquivo `.env`

```bash
cp .env.example .env
```

### 3. **Construção e Execução com Docker**

Para construir e rodar a imagem Docker, execute:

```bash
docker compose up --build -d
```

(Certifique-se de o docker desktop estar aberto)

### 4. **Execute o backend e a API**

4.1. Navegue até a pasta do app:

```bash
cd app/
```

4.2. Inicie o arquivo `main.py`:

```bash
python3 ./main.py
```

Agora você verá a execução dos testes e lógo após iniciando a API localmente.

### 5. **Executando Testes e Interagindo com a API via Postman**

- Baixar no Google Drive: [Coleção Postman](https://drive.google.com/file/d/1FoVy6rLrWUo8AqzCyLH0bLei9BdgXrnX/view?usp=sharing)

- Acessar via Postman Web: [Acessar via Postman Web](https://jacksonsantos-448800.postman.co/workspace/Jackson-Santos's-Workspace~22dc40f1-7ade-4169-8a28-087b5ac9e885/collection/43615751-0271e10e-fd61-4868-a2e5-215a91c2c045?action=share&creator=43615751)

### 6. **Exibindo o Front End com Vue.js**

6.1. Com a API ativa, abra um novo terminal e acesse a pasta frontend

```bash
cd frontend/
```

6.2. Instale as dependencias e rode o projeto:

```bash
pnpm install
pnpm run dev
```

O projeto irá rodar em http://localhost:3000/ e você já verá a tabela com os dados e um input de busca para realizar consultas na tabela.

## Observações

- Certifique-se de que a API esteja em execução antes de iniciar o front end.
- Verifique se as portas da API e do front end não estão em conflito com outros serviços.
- Em caso de falha nos testes da API, verifique o console para identificar e corrigir os erros.

### Os arquivos do teste estão localizados na pasta de **Downloads** dentro de /app

- Teste 1 ➜ **downloads/rol_procedimentos**
- Teste 2 ➜ **downloads/data_transform**
- Teste 3.1 ➜ **downloads/data/2023 e 2024**
- Teste 3.2 ➜ **downloads/data/operadoras**
- Teste 3.5 ➜ **downloads/data**

## Agradecimento

Quero agradecer por essa oportunidade. Foi um desafio e tanto, mas aprendi muita coisa no processo. Se pintarem dúvidas, estou por aqui!

📩 E-mail: contato@devjackson.tech
