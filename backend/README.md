# Teste de Desenvolvedor - Intuitive

Este é um projeto de teste para a empresa Intuitive. Siga as instruções abaixo para configurar e rodar o projeto na sua máquina.

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

### 2. **Configure as variáveis de ambiente**

Copie o arquivo `.env.example` e crie o arquivo `.env`

```bash
cp .env.example .env
```

### 3. **Construção e Execução com Docker**

Para construir e rodar a imagem Docker, execute:

```bash
docker compose up --build -d
```

### 4. **Instale as dependências do backend**

O projeto utiliza bibliotecas como pandas, pdfplumber e outras para otimização. Rode o seguinte comando:

```bash
docker build -t test_intuitive .
```
### 5. **Execute o backend e a API**

1. Navegue até a pasta do backend:

```bash
cd backend/app
```

2. Execute o arquivo main.py para rodar a aplicação e instalar automaticamente as dependências necessárias.
