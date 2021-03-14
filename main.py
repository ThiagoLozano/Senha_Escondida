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
        while True:
            print("\n********** LOGIN ******************")
            name = str(input("Digite seu nome: "))
            password = getpass.getpass("Digite sua Senha: ")

            if name == self.credenc['Credentials']['Login'] and password == self.credenc['Credentials']['Password']:
                print("Login efetuado com sucesso.")
                print("Bem vindo {}\n".format(self.credenc['User']))
                break
            else:
                print("ERROR: Nome ou Senha estão incorretos")
                break


usuario = Cadastro()
