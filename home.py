# Obrigado por usar o Home!

# Crie dois arquivos TXT, "nome.txt", "senha.txt" e "logado.txt"

import requests
from colorama import Fore, init
import os
import time

init()
PASSKEY = open("senha.txt", "r")
def LIMPAR_TERMINAL():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def TELA_INICIAL():
    # Função inutil so pra minha logica dar certo(deu)
    print("HOI BATATA, NAO MUDE MEU CODIGO (:")

CODIGO = ""
def VERIFICAR_CODIGO_NITRO(CODIGO):
    print(r"""

    __      ________ _____  _____ ______ _____ _____          _____   ____  _____  
    \ \    / /  ____|  __ \|_   _|  ____|_   _/ ____|   /\   |  __ \ / __ \|  __ \ 
     \ \  / /| |__  | |__) | | | | |__    | || |       /  \  | |  | | |  | | |__) |
      \ \/ / |  __| |  _  /  | | |  __|   | || |      / /\ \ | |  | | |  | |  _  / 
       \  /  | |____| | \ \ _| |_| |     _| || |____ / ____ \| |__| | |__| | | \ \ 
        \/   |______|_|  \_\_____|_|    |_____\_____/_/    \_\_____/ \____/|_|  \_\
                                                                                                                                                            
    """)
    url = f"https://discord.com/api/v9/entitlements/gift-codes/{CODIGO}?with_application=false&with_subscription_plan=true"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    resposta = requests.get(url, headers=headers)
    CODIGO = input(Fore.YELLOW + "Codigo para verificar\n>> ")
    if CODIGO.lower() == "/home":
        print(Fore.YELLOW + "\nVoltando para Home...\n")
        TELA_INICIAL()
         
    if resposta.status_code == 200:
        dados = resposta.json()
        if dados.get("redeemed"):
            print(Fore.YELLOW + "\n[RESGATADO]: O código já foi usado!\n")
            VERIFICAR_CODIGO_NITRO(CODIGO)
        elif dados.get("expires_at"):
           print(Fore.RED + "\n[EXPIRADO]: O código já passou do prazo!\n")
        else:
            print(Fore.GREEN + "\n[VÁLIDO]: O código pode ser resgatado!\n")
            VERIFICAR_CODIGO_NITRO(CODIGO)
    elif resposta.status_code == 404:
        print(Fore.MAGENTA + "\n[INDEFINIDO]: Código não encontrado ou inválido!\n")
        VERIFICAR_CODIGO_NITRO(CODIGO)
    else:
        print(Fore.RED + "\n[ERRO]: Não foi possível verificar o código!\n")
        VERIFICAR_CODIGO_NITRO(CODIGO)

def PASSWORD():
    global PASS_CHOOSE
    PASS_CHOOSE = input(Fore.YELLOW + "Escolha uma senha\n>> ")
    if len(PASS_CHOOSE) >= 5:
        with open("senha.txt", "w") as PASSKEY:
            PASSKEY.write(PASS_CHOOSE)
        with open("logado.txt", "w") as LOGGED:
            LOGGED.write("YES")
        TELA_INICIAL()
    else:
        print(Fore.RED + "\nSua senha deve conter 5 ou mais caracteres.\n")
        PASSWORD()

def NAME():
    global NAME_CHOOSE
    NAME_CHOOSE = input(Fore.YELLOW + "Digite um apelido para você\n>> ")
    if len(NAME_CHOOSE) >= 3:
        with open("nome.txt", "w") as USER_NAME:
            USER_NAME.write(NAME_CHOOSE)
        PASSWORD()
    else:
        print(Fore.RED + "\nSeu apelido deve conter 3 ou mais caracteres.\n")
        NAME()

if os.path.exists("nome.txt"):
    with open("nome.txt", "r") as USER_NAME:
        USER_NAME2 = USER_NAME.read().strip()

def TELA_INICIAL():
    LIMPAR_TERMINAL()
    print(Fore.YELLOW + f"""
    
     _    _  ____  __  __ ______ 
    | |  | |/ __ \|  \/  |  ____|
    | |__| | |  | | \  / | |__   
    |  __  | |  | | |\/| |  __|  
    | |  | | |__| | |  | | |____ 
    |_|  |_|\____/|_|  |_|______|
       Bem vindo, {USER_NAME2}                                             
 """)
    PROGRAM = input(Fore.YELLOW + "Qual programa você vai usar?\n>> ")
    PROGRAM = PROGRAM.lower()

    if PROGRAM == "verificador":
        LIMPAR_TERMINAL()
        VERIFICAR_CODIGO_NITRO(CODIGO)

def LOGGED2():
    if os.path.exists("logado.txt"):
        with open("logado.txt", "r") as LOGGED:
            status = LOGGED.read().strip()
        if status == "YES":
            if os.path.exists("nome.txt"):
                with open("nome.txt", "r") as USER_NAME:
                    USER_NAME2 = USER_NAME.read().strip()
                    PASSWORD2 = PASSKEY.read().strip()
                VERIFY = input(Fore.YELLOW + "Digite sua senha do Home\n>>")
                if VERIFY == PASSWORD2:
                    print(Fore.GREEN + f"Logado como {USER_NAME2}!")
                    time.sleep(1)
                    TELA_INICIAL()
                else:
                    print(Fore.RED + "\nParece que a sua senha esta errada.\n")
                    LOGGED2()
            else:
                print(Fore.RED + "Crie um arquivo chamado nome.txt para usar o Home corretamente, burroide.")
                time.sleep(10)
                TELA_INCIAL
        else:
            NAME()
    else:
        NAME()
with open("logado.txt", "r") as LOGGED:
    status = LOGGED.read().strip()
if status == "YES":
    LOGGED2()
else:
    NAME()
