import getpass
import json


class Cadastro:
    def __init__(self):
        # Abre o arquivo JSON.
        with open('./credenciais.json', 'r') as f:
            self.credenc = json.load(f)
        self.Get_Login()

    def Get_Login(self):
        while True:
            print("\n********** LOGIN ******************")
            name = str(input("Digite seu Login: "))
            password = getpass.getpass("Digite sua Senha: ")

            if name == self.credenc['Credentials']['Login'] and password == self.credenc['Credentials']['Password']:
                print("\nLogin efetuado com sucesso!")
                print(f"Bem-vindo(a), {self.credenc['User']}.\n")
                break
            else:
                print("ERROR: Nome ou Senha estão incorretos")
                break


usuario = Cadastro()
