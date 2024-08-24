# Cadastro de Usuários - Django CRUD

Este projeto é uma aplicação Django que implementa um CRUD (Create, Read, Update, Delete) para gerenciamento de usuários. A aplicação permite cadastrar, listar, editar e excluir usuários.

_Obs: Tive um problema durante a confecção do código e acabei não conseguindo concluí-lo. Ele estava pronto, mas na tentativa de melhorar ainda mais, acabei piorando o código e enchendo de bugs. Aqui se encontra o máximo que eu consegui chegar dentro do prazo estipulado._

## Introdução

Este projeto é um exemplo básico de uma aplicação CRUD utilizando Django. O CRUD permite a criação, leitura, atualização e exclusão de informações relacionadas a usuários. A aplicação usa o Django como framework web para gerenciar e manipular dados dos usuários.

## Pré-requisitos

Antes de começar, você precisará ter o Python e o Django instalados no seu ambiente. Certifique-se de ter os seguintes pré-requisitos:

- Python 3.x
- Django 5.x

## Instalação

1. **Clone o Repositório**

   Primeiro, clone o repositório para sua máquina local:

   ```bash
   git clone <https://github.com/aspandrade/projeto-fabrica-2024.2>
   
2. **Navegue para o Diretório do Projeto**

- cd nome_do_seu_repositorio

3. Crie um Ambiente Virtual

- python -m venv env

4. Ative o Ambiente Virtual 

- no Windows = .\env\Scripts\activate
- no macOS/Linux = source venv/bin/activate

5. Instale as Dependências

- pip install -r requirements.txt

6. Execute as Migrações

- python manage.py makemigrations
- python manage.py migrate

7. Inicie o Servidor

- python manage.py runserver

**A aplicação oferece as seguintes funcionalidades:**

Página Inicial: http://127.0.0.1:8000/ - Página inicial com um formulário para cadastro de novos usuários.
Listagem de Usuários: http://127.0.0.1:8000/usuarios/ - Visualize a lista de usuários cadastrados.
Criar Usuário: http://127.0.0.1:8000/usuarios/criar/ - Formulário para criar um novo usuário.
Editar Usuário: http://127.0.0.1:8000/usuarios/editar/<id>/ - Formulário para editar um usuário existente, onde <id> é o ID do usuário.
Excluir Usuário: http://127.0.0.1:8000/usuarios/deletar/<id>/ - Página para confirmar a exclusão de um usuário, onde <id> é o ID do usuário.
Estrutura do Projeto
app_cad_usuarios/: Diretório da aplicação que contém o código principal.
migrations/: Diretório de migrações do banco de dados.
templates/: Diretório que contém os templates HTML.
views.py: Contém as views que manipulam as requisições e renderizam as páginas.
models.py: Define o modelo de dados Usuario.
forms.py: Define o formulário para o modelo Usuario.
urls.py: Define as URLs da aplicação.
Contribuição
Se você deseja contribuir com o projeto, por favor siga as seguintes etapas:

Faça um fork do repositório.
Crie uma branch para suas modificações.
Faça commit das suas alterações.
Abra um pull request para revisão.
Licença
Este projeto está licenciado sob a Licença MIT.

Agradecimentos
Obrigado por usar este projeto CRUD Django para gerenciamento de usuários. Se você tiver alguma dúvida ou precisar de assistência, sinta-se à vontade para entrar em contato.

Boa sorte e divirta-se codificando!