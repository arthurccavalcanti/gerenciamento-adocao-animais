# TO DO
- [ ] interface CLI
- [ ] interface GUI
- [ ] funções de match
- [x] integrar main com outros arquivos
- [ ] banco de dados

# ESTRUTURA:

```
adocao-animais/
├── main.py                  
├── perfis/
│   ├── __init__.py
│   ├── pets.py            
│   ├── adotantes.py            
│   ├── voluntarios.py          
├── match/
│   ├── __init__.py
│   ├── match_pet.py
│   ├── match_voluntario.py
├── armazenamento/
│   ├── __init__.py
│   ├── armazenamento_json.py
│   ├── armazenamento_db.py       
├── testes/
│   ├── __init__.py
│   ├── testes.py
├── interface/
│   ├── __init__.py
│   ├── cli_interface.py
│   ├── gui_interface.py               
├── config.py                 
├── requirements.txt          
└── README.md
```

# FLUXO DE PROGRAMA:


_CRUD_:
```
main -> menu principal -> menu crud -> perfil -> operações crud -> menu principal
```


_MATCH_
```
main -> menu principal -> menu match -> match voluntario/pet -> menu principal
```
