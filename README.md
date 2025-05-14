# TO DO
- [ ] interface CLI
- [ ] interface GUI
- [ ] funções de match
- [ ] integrar main com outros arquivos
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
│   ├── match-animal-adotante.py
│   ├── match-voluntario.py
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
main -> CLI/GUI (Recebe do usuário operação CRUD e perfil a ser modificado) -> Perfis (recebem e validam dados, chamam funções de armazenamento e retornam resultado) -> main (recebe resultados) -> CLI/GUI (exibe resultados, pergunta se usuário deseja nova operação)
```


_MATCH_
```
main -> CLI/GUI (Recebe do usuário tipo de match: voluntário x adotante-animal, geral x perfil específico) -> Match (Recebe dados do usuário, acessa dados armazenados, realiza algoritmo) -> main (recebe resultados) -> CLI/GUI (exibe resultados, pergunta se usuário deseja realizar novo match)
```
