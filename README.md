# comunidadeimpressionadora
Projeto de desenvolvimento web com Python utilizando Flask, Bootstrap(v5.0), HTML, CSS. 

Projeto web em python de site em formato de blog. Contém tela de login e criação de usuários com integração em banco de dados para armazenamento de dados de usuários. 


Uma plataforma web de rede social e gerenciamento de conhecimento projetada para engajar membros, permitindo o compartilhamento de ideias, artigos e o acompanhamento de conquistas educacionais. Desenvolvida utilizando a arquitetura clássica **MVT (Model-View-Template)** com o ecossistema robusto do **Flask**, Python e banco de dados relacional.

---

## 💡 Sobre o Projeto

A **Comunidade Impressionadora** vai além de um simples blog: trata-se de um ecossistema completo onde usuários cadastrados podem gerenciar seus perfis, expor em quais cursos ou tecnologias estão especializados (através de um sistema dinâmico de Badges/Tags) e interagir através de publicações interativas (*Posts*). 

Este repositório foi construído seguindo rigorosas boas práticas de desenvolvimento web, incluindo criptografia de ponta a ponta para senhas, validação server-side de formulários e renderização dinâmica via jinja2 com componentes responsivos integrados ao **Bootstrap**.

---

## ✨ Funcionalidades Principais (Features)

* **🔐 Sistema de Autenticação Seguro (Auth-Flow):** Registro e login de usuários gerenciados via `Flask-Login` com senhas protegidas com hashing `Bcrypt`. Restrição de rotas privadas apenas para usuários autenticados.
* **✍️ Engine de Microblogging:** CRUD completo de publicações (Criar, Exibir, Editar e Excluir posts) com suporte a textos longos e formatação flexível.
* **👤 Perfil customizável com Upload de Mídia:** Cada membro possui uma página dedicada onde pode atualizar suas informações, escolher os cursos que concluiu e realizar o upload de fotos de perfil personalizadas (com processamento e redimensionamento automático de imagem via biblioteca `PIL/Pillow`).
* **🏅 Sistema Dinâmico de Badges:** Exibição inteligente dos cursos e especializações do usuário em seus respectivos posts e cards de perfil, facilitando o networking dentro da plataforma.
* **🛡️ Segurança de Dados Avançada:** Proteção nativa contra ataques CSRF (Cross-Site Request Forgery) em todos os formulários através de tokens injetados dinamicamente via `Flask-WTF`.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando um ecossistema tecnológico moderno focado em performance, legibilidade de código e escalabilidade:

* **Backend:** [Python](https://www.python.org/) & [Flask Framework](https://flask.palletsprojects.com/)
* **Persistência de Dados & ORM:** [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) (Abstração de banco de dados relacional / SQLite para desenvolvimento)
* **Formulários & Validação:** [Flask-WTF](https://flask-wtf.readthedocs.io/) & [WTForms](https://wtforms.readthedocs.io/)
* **Segurança:** [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/) (Criptografia) & [Flask-Login](https://flask-login.readthedocs.io/) (Gerenciamento de Sessão)
* **Manipulação de Imagem:** [Pillow (PIL)](https://pillow.readthedocs.io/)
* **Frontend UI:** HTML5, CSS3, Jinja2 Templates e [Bootstrap 5](https://getbootstrap.com/)

---

## 📂 Arquitetura do Sistema e Módulos do Código

O projeto adota o padrão de organização modular, centralizado em um pacote de aplicação (`comunidadeimpresssionadora`):

### 🐍 Core Backend (`Python`)
* **`__init__.py`**: O coração da aplicação. Inicializa a instância do Flask, configura variáveis de ambiente seguras (`SECRET_KEY`), define o banco de dados SQL e gerencia o ciclo de vida dos plugins (`Bcrypt`, `LoginManager`).
* **`models.py`**: Camada de dados (Database Blueprint). Define os esquemas e relacionamentos do banco de dados (Relacionamento de Um-para-Muitos entre `Usuario` e `Post`), utilizando métodos avançados de lazy loading e mapeamento de chaves estrangeiras.
* **`forms.py`**: Centraliza as regras de negócio de validação. Contém algoritmos personalizados (`validate_email`, `validate_username`) para impedir duplicidade de cadastros em tempo de execução, além de filtros para formatos de arquivos permitidos (`FileAllowed`).
* **`routes.py`**: Controlador de tráfego (Controller). Orquestra os endpoints da aplicação, as requisições HTTP (GET/POST), mensagens de feedback instantâneo ao usuário (`Flash Messages`) e a lógica de persistência no banco (`db.session.commit`).

### 🎨 Camada de Visão (`Templates HTML`)
* **`navbar.html`**: Menu de navegação global e reativo. Adapta-se dinamicamente exibindo opções contextuais baseadas no estado de login do usuário (`current_user.is_authenticated`).
* **`homepage.html`**: O feed principal da comunidade, estruturado em colunas para destacar os dados do autor (com suas respectivas badges de cursos) ao lado do conteúdo da publicação.
* **`perfil.html` & `editar_perfil.html`**: Painel do usuário (*Dashboard*) que renderiza as métricas da conta (número de posts e cursos) e injeta de forma integrada o formulário multipart (`enctype="multipart/form-data"`) para atualização de fotos e dados.
* **`login_criarconta.html`**: Interface unificada de onboarding do usuário, tratando mensagens de erro e feedback de campos inválidos de forma nativa e elegante.
* **`criar_post.html`**: Editor de texto limpo para publicação rápida de conteúdo na rede.

---

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Gerenciador de pacotes `pip`.

## 📈 Próximos Passos (Roadmap de Evolução)

* [ ] Implementar sistema de comentários em tempo real abaixo dos posts.
* [ ] Adicionar botão de "Curtir" (Like) utilizando requisições assíncronas (AJAX/Fetch API).
* [ ] Migrar o banco de dados de desenvolvimento (SQLite) para produção (PostgreSQL).
* [ ] Implementar sistema de paginação de posts na Homepage para otimizar o tempo de carregamento da aplicação.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.

```

```
