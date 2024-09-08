
# 007 Django 4 Custom 404 Error Page

### O que é uma Página de Erro 404 Personalizada?

Uma página de erro 404 personalizada melhora a experiência do usuário ao fornecer uma mensagem clara e útil quando uma página não é encontrada. No Django, você pode criar uma página de erro 404 personalizada simplesmente adicionando um arquivo `404.html` no diretório de templates e ajustando as configurações para servir esta página.

## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12 com PIP e venv**

- **No [repositório 001](https://github.com/Django-Dev-Br/001-django4-basic-project) há explicações sobre PIP e venv**
  
  [Baixar Python 3.12](https://www.python.org/downloads/release/python-3122/)

   Confira o vídeo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual):
  [![Watch the video](https://img.youtube.com/vi/eetDeQrv0Rs/0.jpg)](https://youtu.be/eetDeQrv0Rs)

- **Virtualenv**

  Para instalar o pacote `virtualenv` no Python, utilize os seguintes comandos:

  - **Linux**:
    ```bash
    python3 -m pip install virtualenv
    ```

  - **Windows**:
    ```bash
    python -m pip install virtualenv
    ```

### Passos para Executar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Django-Dev-Br/007-Django-4-Custom-404-Error-Page.git
    cd 007-Django-4-Custom-404-Error-Page
    ```

2. **Crie um ambiente virtual**:
   
    **Windows**
    ```bash
     python -m venv myvenv  
    ```
   **Linux**
    ```bash
     python3 -m venv myvenv  
    ```

3. **Ative o ambiente virtual criado**:
   
    **Windows**
    ```bash
    myvenv\Scripts\activate  
    ```

   **Linux**
    ```bash
    source myvenv/bin/activate  
    ```

4. **Instale o Django**:
    ```python
    pip install django==4.2.15
    ```

5. **Acesse a pasta do repositório**:
    ```bash
    cd 007-Django-4-Custom-404-Error-Page
    ```
    
6. **Configurar uma Página de Erro 404 Personalizada**:

    - Crie uma pasta chamada templates em seu App Django
    - Crie um arquivo chamado `404.html` dentro da pasta supracitada.
    - Adicione o seguinte conteúdo ao arquivo `404.html`:

    ```html
    <!-- 404.html -->
    <!DOCTYPE html>
    <html>
    <head>
        <title>Página Não Encontrada</title>
    </head>
    <body>
        <h1>Erro 404</h1>
        <p>Desculpe, a página que você está procurando não foi encontrada.</p>
    </body>
    </html>
    ```

    - Certifique-se de que seu `settings.py` inclua a configuração para usar a página de erro 404 personalizada:

    ```python
    # settings.py
    DEBUG = False
    ALLOWED_HOSTS = ['*']  
    ```

7. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

### Testando a Página de Erro 404

- Acesse uma URL inexistente no seu navegador, por exemplo: [http://127.0.0.1:8000/nao-existe](http://127.0.0.1:8000/nao-existe)
- Você verá a página de erro 404 personalizada que você configurou.


### Estrutura de Diretórios do Projeto

```
007-django4-custom-404-error-page/
├── myproject/
│   ├── __init__.py      # Marca o diretório como um pacote Python
│   ├── asgi.py          # Configurações para o servidor ASGI (usado para aplicações assíncronas)
│   ├── settings.py      # Configurações do projeto (incluindo ALLOWED_HOSTS e DEBUG)
│   ├── urls.py          # Mapeamento de requisições HTTP e redirecionamento para os templates HTML
│   └── wsgi.py          # Configurações para o servidor WSGI (usado para servir a aplicação)
├── myapp/
│   ├── __init__.py      # Marca o diretório como um pacote Python
│   ├── apps.py          # Configurações do app
│   ├── views.py         # Funções de view para o app
│   └── templates/
│       └── 404.html     # Página de erro 404 personalizada
└── manage.py            # CLI do Django, um script de linha de comando para tarefas administrativas do Django
```

### Sobre Nosso Treinamento Prático-Profissional com projeto real para iniciantes e avançados em web DevOps Full-stack com Python, Django, Bootstrap e Linux.

[Django Developers Brasil - Aprenda programando enquanto programa aprendendo!](https://django.dev.br/)

Nosso treinamento oferece uma experiência prática de aprendizado de programação, adequada tanto para iniciantes quanto para desenvolvedores avançados. Você participará de um projeto real de desenvolvimento de software em um ambiente corporativo autêntico, onde pessoas com diferentes níveis de conhecimento irão colaborar, aprendendo umas com as outras.

**Junte-se a nós!** E desenvolva as habilidades necessárias para o mercado de trabalho, aprimorando tanto seus conhecimentos técnicos quanto suas soft skills em um ambiente colaborativo e realista.
