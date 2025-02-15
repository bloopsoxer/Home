# Obrigado por usar o Home!

# Crie três arquivos TXT, "nome.txt", "senha.txt" e "logado.txt"

import requests
from colorama import Fore, init
import os
import time
import getpass
from datetime import datetime
import threading
import random

def TELA_INICIAL():
    print("Coisa so pro meu codigo dar certo...")

def atualizar_hora():
    agora = datetime.now().time()
    print(f"A hora atual é: {agora.strftime('%H:%M:%S')}")
    time.sleep(1)


def REPETIDOR():
    REPETIR = input(Fore.YELLOW + "Oque o programa vai repetir?\n>> ")
    if REPETIR.lower() == "/home":
        print(f"Programa: {REPETIR}\n| Caracteres: " + f"{len(REPETIR)}\n")
        TELA_INICIAL()
    REPETIDOR()

def senha(prompt='Digite algo\n>> '):
    return getpass.getpass(prompt=prompt)

def checa_se_numeros(s):
    return s.isdigit()

def DADO():
    FIRST = input("Escolha quantos lados tem o dado!\n>> ")
    if checa_se_numeros(FIRST):
        FIRST = int(FIRST)
        print(random.randint(1, FIRST))
    else:
        print(Fore.RED + f"{FIRST} não é numero!")




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

import os
import platform

def SUSPENDER():
    SISTEMA = platform.system()

    try:
        if SISTEMA == "Windows":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif SISTEMA == "Linux":
            os.system("systemctl suspend")
        elif SISTEMA == "Darwin":  # macOS
            os.system("pmset sleepnow")
        else:
            print(f"Sistema operacional {sistema_operacional} não suportado para esta operação.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def TELA_INICIAL():
    LIMPAR_TERMINAL()
    print(Fore.YELLOW + fr"""
    
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
        print(Fore.YELLOW + r"""

    __      ________ _____  _____ ______ _____ _____          _____   ____  _____  
    \ \    / /  ____|  __ \|_   _|  ____|_   _/ ____|   /\   |  __ \ / __ \|  __ \ 
     \ \  / /| |__  | |__) | | | | |__    | || |       /  \  | |  | | |  | | |__) |
      \ \/ / |  __| |  _  /  | | |  __|   | || |      / /\ \ | |  | | |  | |  _  / 
       \  /  | |____| | \ \ _| |_| |     _| || |____ / ____ \| |__| | |__| | | \ \ 
        \/   |______|_|  \_\_____|_|    |_____\_____/_/    \_\_____/ \____/|_|  \_\
                                                                                                                                                            
    """)
        VERIFICAR_CODIGO_NITRO(CODIGO)
        
    elif PROGRAM == "/help":
        print(Fore.YELLOW + """Programas disponiveis:

| VERIFICADOR: Verifica um codigo de nitro do Discord.
| EXIT: Sai do Home.
| SUSPEND: Suspende o computador.
| REPEAT: Repete alguma frase.
| DADO: Gira um dado.  
| HORA: Diz o horario atual.
              """)
        senha("Aperte enter para sair do Help.")
        TELA_INICIAL()

    elif PROGRAM == "exit":
        LIMPAR_TERMINAL()
        print(Fore.RED + "\nSaindo...\n")
        exit()

    elif PROGRAM == "suspend":
        SUSPENDER()
    elif PROGRAM == "repetidor":
        LIMPAR_TERMINAL()
        print(Fore.YELLOW + r"""

     _____  ______ _____  ______ _______ _____ _____   ____  _____  
    |  __ \|  ____|  __ \|  ____|__   __|_   _|  __ \ / __ \|  __ \ 
    | |__) | |__  | |__) | |__     | |    | | | |  | | |  | | |__) |
    |  _  /|  __| |  ___/|  __|    | |    | | | |  | | |  | |  _  / 
    | | \ \| |____| |    | |____   | |   _| |_| |__| | |__| | | \ \ 
    |_|  \_\______|_|    |______|  |_|  |_____|_____/ \____/|_|  \_\
                                                                                                                              
    """)

        REPETIDOR()
    elif PROGRAM == "dado":
        LIMPAR_TERMINAL()
        DADO()
    elif PROGRAM == "hora":
        atualizar_hora()
        TELA_INICIAL()
    else:
        print(Fore.RED + f"\n\"{PROGRAM}\" Não esta definido, digite \"/help\" para ver todos os programas disponiveis.")
        time.sleep(1)
        TELA_INICIAL()

def LOGGED2():
    if os.path.exists("logado.txt"):
        with open("logado.txt", "r") as LOGGED:
            status = LOGGED.read().strip()
        if status == "YES":
            if os.path.exists("nome.txt"):
                with open("nome.txt", "r") as USER_NAME:
                    USER_NAME2 = USER_NAME.read().strip()
                    PASSWORD2 = PASSKEY.read().strip()
                VERIFY = senha(Fore.YELLOW + "Digite sua senha do Home\n>> ")
                if VERIFY == PASSWORD2:
                    print(Fore.GREEN + f"\nLogado como {USER_NAME2}!\n")
                    time.sleep(1)
                    TELA_INICIAL()
                if len(VERIFY) == 0:
                    print(Fore.RED + "\nSua senha tem mais que 0 caracteres.\n")
                    LOGGED2()
                else:
                    print(Fore.RED + "\nAcesso negado.\n")
                    time.sleep(1)
                    LOGGED2()
            else:
                print(Fore.RED + "Crie um arquivo chamado nome.txt para usar o Home corretamente, burroide.")
                time.sleep(10)
                TELA_INCIAL()
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


black_background = "\033"
