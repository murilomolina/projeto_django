# Projeto Django - Guia de Configuração e Execução

Este guia fornece um passo a passo para configurar o ambiente virtual, iniciar o projeto Django, rodar o servidor e criar uma aplicação no Django.

---

## 1. Configuração do Ambiente Virtual

Primeiro, crie e ative um ambiente virtual para gerenciar as dependências do projeto.

```bash
# Crie o ambiente virtual
...\django_py> python -m venv venv

# Defina a política de execução no PowerShell (caso necessário)
...\django_py> set-ExecutionPolicy -Scope CurrentUser Unrestricted

# Ative o ambiente virtual
...\django_py> venv\Scripts\Activate.ps1
```

> **Nota:** `...\django_py>` representa o diretório onde você iniciou o projeto. Substitua pelo seu caminho específico.

---

## 2. Instalação e Inicialização do Projeto Django

Com o ambiente virtual ativo, instale o Django e inicie um novo projeto.

```bash
# Instale o Django
(venv) ...\django_py> pip install django

# Inicie o projeto
(venv) ...\django_py> django-admin startproject primeiro_projeto
```

---

## 3. Inicialização do Servidor de Desenvolvimento

Para rodar o servidor Django, abra um novo terminal e execute os comandos abaixo.

```bash
# Defina a política de execução no novo terminal (caso necessário)
...\django_py\primeiro_projeto> set-ExecutionPolicy -Scope CurrentUser Unrestricted

# Ative o ambiente virtual no novo terminal
...\django_py\primeiro_projeto> ..\venv\Scripts\Activate.ps1

# Rode o servidor
(venv) ...\django_py\primeiro_projeto> python manage.py runserver
```

> O servidor estará disponível em `http://127.0.0.1:8000/`.

---

## 4. Criação de uma Aplicação Django

Para organizar o projeto, você pode usar outro terminal para criar uma nova aplicação.

```bash
# Acesse o diretório do projeto
...\django_py> cd primeiro_projeto

# Defina a política de execução (caso necessário)
...\django_py\primeiro_projeto> set-ExecutionPolicy -Scope CurrentUser Unrestricted

# Ative o ambiente virtual no novo terminal
...\django_py\primeiro_projeto> ..\venv\Scripts\Activate.ps1

# Crie a aplicação
(venv) ...\django_py\primeiro_projeto> python manage.py startapp primeira_aplicacao
```

---

## Estrutura do Projeto

Após seguir os passos acima, a estrutura básica do projeto ficará assim:

```
django_py/
├── primeiro_projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── primeira_aplicacao/
│   ├── migrations/
│   ├── __init__.py
│   ├── views.py
│   └── ...
└── venv/
```
