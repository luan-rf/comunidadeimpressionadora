# Comunidade Impressionadora

Uma aplicação web em formato de blog e rede social desenvolvida em Python com o framework Flask. O sistema adota a arquitetura de organização modular para gerenciar autenticação de usuários, controle de sessões, persistência de dados estruturados com relacionamentos no banco de dados, upload de arquivos de mídia com redimensionamento automático e validação de formulários no lado do servidor.

## 🛠️ Tecnologias Utilizadas

*   **Python 3**
*   **Flask** (Framework Web)
*   **Flask-SQLAlchemy** (ORM e Integração com Banco de Dados)
*   **Flask-Bcrypt** (Mecanismo de Hashing para Senhas)
*   **Flask-Login** (Gerenciador de Autenticação e Sessões)
*   **Flask-WTF & WTForms** (Estruturação e Validação de Formulários com Tokens CSRF)
*   **Pillow (PIL)** (Processamento e Redimensionamento Gráfico de Imagens)
*   **SQLite** (Banco de Dados Relacional local)
*   **Bootstrap 5** (Estilização Front-End Responsiva)

---

## 📂 Estrutura e Arquitetura do Sistema

```text
├── comunidadeimpressionadora/
│   ├── static/
│   │   ├── css/
│   │   └── fotos_perfil/      # Armazenamento das fotos de perfil dos usuários
│   ├── templates/             # Arquivos de visualização (Jinja2)
│   │   ├── base.html
│   │   ├── criar_post.html
│   │   ├── editarperfil.html
│   │   ├── homepage.html
│   │   ├── login.html
│   │   ├── navbar.html
│   │   └── perfil.html
│   ├── __init__.py            # Inicialização da App, Configurações e Instâncias das Extensões
│   ├── forms.py               # Estrutura dos formulários e métodos de validação customizados
│   ├── models.py              # Definição das tabelas e relacionamentos do banco de dados
│   └── routes.py              # Declaração dos endpoints e lógica de negócios das rotas
├── instance/
│   └── db_comunidade.db       # Banco de dados SQLite local gerado
├── .gitignore
├── criar_banco.py             # Script utilitário para provisionamento das tabelas
├── main.py                    # Ponto de entrada para execução do servidor
└── segredos.py                # Arquivo de chaves locais (Protegido via .gitignore)

```

---

## ⚙️ Funcionalidades Implementadas

* **Controle de Acesso e Sessão (Auth Flow)**: Fluxo completo de registro e login via `Flask-Login`. As senhas passam por processo de hashing seguro através do `Bcrypt` antes do armazenamento no banco de dados. Bloqueio de rotas privadas via decorador `@login_required`.
* **CRUD de Publicações**: Lógica completa para criação, leitura, atualização e exclusão (Create, Read, Update, Delete) de postagens vinculadas ao ID do autor.
* **Módulo de Perfil e Upload Dinâmico**: Painel do usuário para atualização de dados cadastrais, seleção de tags de especialização (Badges de cursos) e alteração de foto de perfil. O processamento de imagem utiliza a biblioteca `Pillow` para realizar o redimensionamento automático do arquivo para otimização de armazenamento.
* **Vínculo Relacional de Badges**: Sistema que associa e exibe os cursos e especializações selecionados pelo usuário diretamente em seus cards e publicações no feed.
* **Segurança em Formulários**: Mecanismo de defesa contra ataques de falsificação de solicitação entre sites (CSRF) implementado de forma nativa em todas as requisições POST através de tokens injetados pelo `Flask-WTF`.

---

## 📄 Licença

Este projeto é distribuído sob os termos da Licença MIT.

```

```
