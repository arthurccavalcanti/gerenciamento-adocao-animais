## ESTRUTURA DE ARQUIVOS:

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
├── armazenamento_json.py  
├── testes.py
├── cli_interface.py                   
├── requirements.txt          
└── README.md
```

## FLUXO DE PROGRAMA:


### _CRUD_:
```
main -> menu principal -> menu crud -> perfil -> operações crud -> menu principal
```


### _MATCH_
```
main -> menu principal -> menu match -> match voluntario/pet -> menu principal
```

## FUNCIONAMENTO DO PROGRAMA

__1 —__ Ao iniciar o programa (executando main.py), o usuário tem a opção de mexer nos dados (CRUD) ou fazer um match baseado nos dados salvos localmente.
Além disso, o usuário pode escolher encerrar o programa e mudar de opção.

__1.1 —__ Se o usuário escolher mexer nos dados, o programa solicita qual perfil ele deseja acessar: adotantes, pets ou voluntários.

O menu também solicita qual operação o usuário deseja fazer: criar, ler, editar ou deletar. Antes de confirmar, o usuário pode voltar ao menu anterior ou mudar a operação que deseja fazer.

__1.1.1 —__ Ao escolher fazer uma operação num perfil, o programa chama a função adequada, que retorna o resultado da operação.

Em seguida, o resultado é exibido ao usuário, que pode escolher fazer outra opção (voltando ao passo 1.1)


__1.2 —__ Se o usuário escolher receber uma match, o programa dá duas opções: mostrar os melhores matches entre um pet e possíveis adotantes ou mostrar os melhores matches entre um voluntário e possíveis adotantes.

Antes de confirmar, o usuário pode voltar ao menu anterior ou mudar O tipo de match que deseja fazer.

__1.2.1 —__ Ao escolher um tipo de match, o programa chama a função adequada, que
- Dá a opção ao usuário de visualizar todas as entradas.
- Recebe do usuário qual adotante/match ele deseja usar para fazer o match.
- Retorna os melhores matches

Novamente, o resultado é exibido ao usuário, que pode escolher fazer outra opção (voltando ao passo 1.2)

## ESTRUTURA DADOS

O arquivo pets.json tem os seguintes campos:
- id
- tipo
- nome
- idade
- sexo
- personalidade
- histórico médico
- raça
- cor
- porte

O arquivo voluntário.json tem os seguintes campos:
- cpf
- nome completo
- data de nascimento
- idade
- endereço
- disponibilidade
- data cadastro
- email
- telefone

O arquivo adotantes.json tem os seguintes campos:
- nome
- cpf
- idade
- profissão
- endereço
- contato