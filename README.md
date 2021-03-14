# PROJETO PYTHON: Senha Escondida

> Script que cria um login dentro de um prompt ocultando a entrada da senha.

# Tecnologias Utilizadas

* **_VScode_**;

* **_Python3;_** 

# Bibliotecas e Configurações

### Bibliotecas Utilizadas

```python
import getpass
import json
```

### Configurações

> O script foi feito com base na estrutura POO.

```python
class Cadastro:
    def __init__(self):

usuario = Cadastro()
```

# Fontes

> https://docs.python.org/pt-br/3/library/getpass.html

### Credenciais JSON

```json
{
    "id": 1,
    "User": "Thiago",
    "Credentials": {
        "Login": "Teste",
        "Password": "123"
    }
}
```

> O __credenciais.json__ serve para armazenar os dados dos usuários já cadastrados no sistema.
>
> __id__: Número de identificação dos usuários.
>
> __User__: Nome do usuário.
>
> __Credentials__:  Objeto que guarda os dados de Login.
>
> __Login__:  Nome de entrada.
>
> __Password__: Senha de entrada.

``` python
1. with open('./credenciais.json', 'r') as f:
2.     self.credenc = json.load(f)
3.     self.Login()
```

> Linha 1: Abre o arquivo JSON e atribui á uma variável __f__
>
> Linha 2: Cria uma variável que recebe o arquivo carregado em JSON.
>
> Linha 3: Chama a função __Login()__



### Login 

```python
1. def Login(self):
2.    while True:
3.        print("\n********** LOGIN ******************")
4.        name = str(input("Digite seu nome: "))
5.        password = getpass.getpass("Digite sua Senha: ")
6.
7.        if name == self.credenc['Credentials']['Login'] and password == self.credenc['Credentials']['Password']:
8.        	print("Login efetuado com sucesso.")
9.        	print("Bem vindo {}\n".format(self.credenc['User']))
10.         break
11.       else:
12.          print("ERROR: Nome ou Senha estão incorretos")
13.          break
```

> Linha 1: Cria a função __Login()__
>
> Linha 2:  Cria um loop.
>
> Linha 3: Imprime um texto na tela.
>
> Linha 4: Cria uma variável que recebe o nome de entrada.
>
> Linha 5: Cria uma variável que recebe a senha de entrada.
>
> Linha 7: Valida se o nome e senha são compatíveis com os dados do JSON.
>
> Linha 8: Imprime um texto na tela.
>
> Linha 9: Imprime um texto na tela.
>
> Linha 10: Fecha o laço.
>
> Linha 11: Cria uma condição contrária.
>
> Linha 12:  Imprime um texto na tela.
>
> Linha 13: Fecha o laço.

# Exemplo

### Windows PowerShell

![Dir](https://github.com/ThiagoLozano/Senha_Escondida/blob/main/Win_PowerShell/Dir.PNG)

![Main](https://github.com/ThiagoLozano/Senha_Escondida/blob/main/Win_PowerShell/Main.PNG)



### Linux

![Dir](https://github.com/ThiagoLozano/Senha_Escondida/blob/main/Linux/Dir.png)

![Main](https://github.com/ThiagoLozano/Senha_Escondida/blob/main/Linux/Main.PNG)
