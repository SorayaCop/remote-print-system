# Remote Print System

Sistema em Django para envio remoto de pedidos e impressão automática em impressora térmica via agente local Windows.

## Stack

- Python
- Django
- SQLite
- Requests
- PyWin32

## Como funciona

Celular → Sistema Web → Notebook da Produção → Impressora USB


## Infraestrutura

Aplicação web hospedada em cloud (Render), permitindo envio remoto de pedidos para agente local conectado à impressora.

## Recursos

Login e senha
Cadastro de pedidos
Impressão automática
Inicialização com Windows
Marcação de pedidos impressos
Caso real

Desenvolvido para pequeno negócio que precisava de solução simples e sem custos mensais.

## Executar
pip install -r requirements.txt <br>
python manage.py migrate
python manage.py runserver
