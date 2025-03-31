# Teste de Desenvolvedor - Intuitive

Este é um projeto de teste para a empresa Intuitive. Siga as instruções abaixo para configurar e rodar o projeto na sua máquina.

## Requisitos

Antes de começar, verifique se você tem as seguintes ferramentas instaladas:

- **Python 3.11+** - Para rodar a aplicação Python
- **Node.js** - Para executar o ambiente de desenvolvimento frontend (caso necessário)
- **MySQL** - Banco de dados utilizado pelo projeto
- **Docker** - Para criar e rodar o contêiner da aplicação

### Para verificar se essas ferramentas estão instaladas:

```bash
python --version
node --version
mysql --version
docker --version
```

**Docker Compose**: Geralmente já incluído no Docker Desktop.
**Git (opcional)**: Para clonar o repositório do projeto.

### Passos para Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/Jacksons357/test_intuitive.git
cd test_intuitive
```

2. **Copie o arquivo `.env.example` e crie o arquivo `.env`**

O arquivo `.env` contém as configurações do ambiente, incluindo variáveis sensíveis como credenciais de banco de dados.

```bash
cp .env.example .env
```

3. **Construir e rodar o contêiner Docker:**

O projeto utiliza Docker para facilitar o ambiente de desenvolvimento. Para construir e rodar a imagem Docker, utilize o seguinte comando:

```bash
docker-compose up --build
```
