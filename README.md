# ESTRUTURA:

```
adocao-animais/
├── main.py                  
├── perfis/
│   ├── __init__.py
│   ├── animal.py            
│   ├── adotante.py            
│   ├── voluntario.py          
├── match/
│   ├── __init__.py
│   ├── match-animal-adotante.py
│   ├── match-voluntario.py
├── armazenamento/
│   ├── __init__.py
│   ├── armazenamento-json.py
│   ├── armazenamento-db.py       
├── testes/
│   ├── __init__.py
│   ├── testes.py
├── interface/
│   ├── __init__.py
│   ├── cli-interface.py
│   ├── gui-interface.py               
├── config.py                 
├── requirements.txt          
└── README.md
```
# FLUXO DE PROGRAMA:

```
main -> CLI/GUI -> Input usuário -> Adicionar/Editar/Deletar/Ler -> Perfis -> Armazenamento (leitura/escrita no json) -> Perfis -> main -> CLI/GUI
main -> CLI/GUI -> Input usuário -> Adicionar/Editar/Deletar/Ler -> Match -> Armazenamento (leitura no json) -> Match -> main -> CLI/GUI
```
