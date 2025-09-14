# wsBackend-Fabrica25.2

# Super Hero Tracker 🦸‍♂️🦹‍♂️

Um projeto Django para buscar e listar heróis e vilões de quadrinhos por ano de primeira aparição, utilizando a API pública de super-heróis da Akabab.

## 📚 Tabela de Conteúdos

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação](#instalacao)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuicao)
- [Autor](#autor)

## 🧮 Sobre o Projeto

Este projeto permite:

- Buscar heróis e vilões por ano de primeira aparição.
- Armazenar históricos de anos com os nomes dos personagens encontrados.
- Editar e deletar registros de anos.
- Visualizar heróis com cards estilizados, com imagens e informações detalhadas.
- Interface moderna com cores inspiradas em quadrinhos, botões chamativos e fonte "heróica".

O projeto utiliza **Django** como framework web e integra **API pública de super-heróis** para buscar dados.

## ⚡Funcionalidades

- [x] Buscar heróis por ano.
- [x] Listar todos os anos cadastrados.
- [x] Editar registros de anos.
- [x] Deletar registros com confirmação.
- [x] Visualização estilizada de heróis (cards com imagem e texto).
- [x] Interface moderna com cores e tipografia inspiradas em quadrinhos.
- [x] Responsividade para diferentes tamanhos de tela.

## 🚀 Tecnologias

- **Python 3.13**  
- **Django 5.2**  
- **HTML5 / CSS3**  
- **API Akabab de Super-Heróis**  
- **Git & GitHub**  

## ⚒️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/super-hero-tracker.git
cd super-hero-tracker

2. Crie o ambiente virtual:

  # macOS / Linux
python3 -m venv venv
source venv/bin/activate
   
  # windows
venv\Scripts\activate
  

3. Instale as dependências:

pip install -r requirements.txt

4. Execute as migrações do Django:

python manage.py migrate

5. Inicie o servidor de desenvolvimento:

python manage.py runserver

6.	Abra o navegador em: http://127.0.0.1:8000/

## Uso

•	Na página inicial, escolha entre buscar por ano ou ver heróis.
•	Para buscar por ano, digite o ano e veja os heróis/vilões que apareceram.
•	Nos registros de anos, você pode editar ou deletar os registros existentes.
•	Cada herói é exibido em um card com imagem à direita e informações à esquerda.

## 🧱 Estrutura do Projeto

super-hero-tracker/
│
├─ projeto/                # Configurações do Django
├─ anos/                   # App responsável pelos anos e heróis
│  ├─ templates/           # HTMLs
│  ├─ static/css/          # Arquivos CSS
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  └─ urls.py
├─ venv/                   # Ambiente virtual (ignorada pelo Git)
├─ requirements.txt
├─ .gitignore
└─ manage.py

## 🥂 Contribuição

Contribuições são bem-vindas!
	1.	Faça um fork do projeto.
	2.	Crie uma branch (git checkout -b feature/nova-funcionalidade).
	3.	Faça suas alterações.
	4.	Commit suas mudanças seguindo o padrão semântico:

  git commit -m "feat: adicionar nova funcionalidade X

  5.	Faça push para sua branch e abra um Pull Request."

## Autor

Arthur Henry Dias Paiva
