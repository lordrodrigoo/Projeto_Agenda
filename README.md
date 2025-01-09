# 📅 Projeto Agenda

Bem-vindo ao **Projeto Agenda**! Este é um aplicativo web desenvolvido para gerenciar contatos de forma eficiente e intuitiva.

## 📋 Índice

- [📖 Sobre o Projeto](#-sobre-o-projeto)
- [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Instalação](#️-instalação)
- [🚀 Uso](#-uso)
- [🤝 Contribuição](#-contribuição)
- [📜 Licença](#-licença)
- [📬 Contato](#-contato)

## 📖 Sobre o Projeto

O **Projeto Agenda** é uma aplicação web que permite aos usuários adicionar, editar, visualizar e excluir contatos. Cada contato inclui informações como nome, telefone e e-mail, imagem(opcional). O objetivo é fornecer uma interface simples e eficaz para o gerenciamento de contatos pessoais ou profissionais.

## 💻 Tecnologias Utilizadas

- 🐍 **Python**
- 🌐 **Django**
- 🎨 **HTML/CSS**
- 🗄️ **SQLite**

## ⚙️ Instalação

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/lordrodrigoo/Projeto_Agenda.git
   cd Projeto_Agenda
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requeriments.txt
   ```

4. **Execute as migrações do banco de dados**:
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação**:
   Abra o navegador e vá para `http://127.0.0.1:8000/`.

