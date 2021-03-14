import getpass
import json


class Cadastro:
    def __init__(self):
        # Abre o arquivo JSON.
        with open('./credenciais.json', 'r') as f:
            self.credenc = json.load(f)
        self.Login()

    # Função que faz o Login.
    def Login(self):
        print("\n********** LOGIN ******************")
        name = str(input("Digite seu nome: "))
        password =  getpass.getpass("Digite sua Senha: ")

        for c in self.credenc:
            if name == c['Credentials']['Login'] and password == c['Credentials']['Password']:
                print("Login efetuado com sucesso.")
                print("Bem vindo {}\n".format(c['User']))
                break
            else:
                print("ERROR: Nome ou Senha estão incorretos")
                break


usuario = Cadastro()
