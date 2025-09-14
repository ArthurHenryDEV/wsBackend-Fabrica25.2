# wsBackend-Fabrica25.2
Desafio da Fábrica de Software 2025.2

# 🦸 Biblioteca de Super-Heróis com Django e API
Um projeto Django para buscar e listar heróis e vilões de quadrinhos por nome ou ano de primeira aparição, utilizando a API pública de super-heróis da Akabab.

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

## ⚡ Funcionalidades

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
<pre>
git clone <url-do-repositorio>
cd meuprojeto
</pre>

2. Crie o ambiente virtual:

  ### macOS / Linux
  <pre>
python3 -m venv venv
source venv/bin/activate
  </pre>
  ### Windows
  <pre>
python -m venv venv
venv\Scripts\activate
  </pre>

3. Instale as dependências:
<pre>
pip install -r requirements.txt
</pre>
4. Execute as migrações do Django:
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>
5. Inicie o servidor de desenvolvimento:
<pre>
python manage.py runserver
</pre>
6.	Abra o navegador em: http://127.0.0.1:8000/ 

## 🧰 Uso

•	Na página inicial, escolha entre buscar por ano ou por heróis/vilões.

•	Para buscar por ano, digite o ano e veja os heróis/vilões que apareceram.

•	Nos registros de anos, você pode editar ou deletar os registros 
existentes.

•	Cada herói é exibido em um card com imagem à direita e informações à  	     esquerda.

## 🧱 Estrutura do Projeto
<pre>
wsBackend-Fabrica25.2/
│
├─ projeto/                  # Pasta principal do Django (settings, urls, wsgi/asgi)
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ asgi.py
│  ├─ templates/             # Templates globais do projeto
│  │  └─ home.html
│
├─ herois/                   # App 1 - Heróis
│  ├─ migrations/
│  ├─ templates/
│  │  └─ herois/             # Templates específicos do app
│  │     ├─ listar_herois.html
│  │     ├─ criar_heroi.html
│  │     ├─ editar_heroi.html
│  │     ├─ deletar_heroi.html
│  │     └─ detalhes_heroi.html
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  └─ urls.py
│
├─ anos/                     # App 2 - Anos
│  ├─ migrations/
│  ├─ templates/
│  │  └─ anos/               # Templates específicos do app
│  │     ├─ listar_anos.html
│  │     ├─ criar_ano.html
│  │     ├─ editar_ano.html
│  │     ├─ deletar_ano.html
│  │     ├─ detalhes_ano.html
│  │     └─ buscar_ano.html
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  └─ urls.py
│
├─ static/                   # Arquivos estáticos globais
│  └─ css/
│     └─ styles.css
│
├─ venv/                     # Ambiente virtual (ignorada pelo Git)
├─ requirements.txt          # Dependências do projeto
├─ .gitignore                # Arquivos/pastas ignorados pelo Git
└─ manage.py                 # Arquivo principal do Django
</pre> 
## 🥂 Contribuição

Contribuições são bem-vindas!
	
 1.	Faça um fork do projeto.
	
 2.	Crie uma branch:
  <pre>
  git checkout -b feature/nova-funcionalidade).
</pre>
 
 3.	Faça suas alterações.
	
 4.	Commit suas mudanças seguindo o padrão semântico:
<pre>
  git commit -m "feat: adicionar nova funcionalidade X
</pre> 
5. Faça push para sua branch e abra um Pull Request."

## ✍️ Autor

Arthur Henry Dias Paiva
