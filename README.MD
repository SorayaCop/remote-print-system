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

Login e senha<br>
Cadastro de pedidos<br>
Impressão automática<br>
Inicialização com Windows<br>
Marcação de pedidos impressos<br>
Caso real

Desenvolvido para pequeno negócio que precisava de solução simples e sem custos mensais.

## Executar
pip install<br> 
-r requirements.txt <br>
python manage.py migrate<br>
python manage.py runserver
