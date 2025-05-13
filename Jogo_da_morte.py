import os
import time
import random
import pyttsx3

def teste_de_sorte():
    n = random.randint(1, 3)
    engine = pyttsx3.init()
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")

    while True:
        try:
            p = int(input("Adivinhe o número (1, 2 ou 3): "))
            if p < 1 or p > 3:
                raise ValueError
            if p == n:
                print("Acertou!")
                return True  # Retorna True se o jogador acertar
            else:
                mensagem = (f''' ERROU, minha Avó faria melhor que isso ....
                              .___.
          /)               ,-^     ^-.
         //               /           \ 
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^
                        Resporta era: {n}.''')
                print(mensagem)
                engine.say("ERROU, minha Avó faria melhor que isso...você MORREU")
                engine.runAndWait()
                os.system("cls")
                return False  # Retorna False se o jogador errar
        except ValueError:
            print("Entrada inválida. Digite 1, 2, 3")

if __name__ == "__main__":
    os.system("cls")
    os.system("color 2")
    print(''' 
******* Bem Vindo ao JOGO DA MORTE *******
          **********************

               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\ 
       ::::::;       ;          OOOOO\ 
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                o
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#                                 ''')

    time.sleep(1)
    print("...")
    print('''Você esta prestes a DEFINIR o RUMO da sua vida ....
                        MORRER ou SOBREVIVER
                            so depende de 
           ___________    ____
    ______/   \__//   \__/____\ 
  _/   \_/  :           //____\\ 
 /|      :  :  ..      /        \ 
| |     ::     ::      \        /
| |     :|     ||     \ \______/
| |     ||     ||      |\  /  |
 \|     ||     ||      |   / | \ 
  |     ||     ||      |  / /_\ \ 
  | ___ || ___ ||      | /  /    \ 
   \_-_/  \_-_/ | ____ |/__/      \ 
                _\_--_/    \      /
               /____             /
              /     \           /
              \______\_________/''')
    time.sleep(1)
    os.system("cls")
    os.system("color 4")
    print("Pressione qualquer tecla para inciar")
    time.sleep(2)
    print("Lento de mais...")
    time.sleep(0.7)
    os.system("cls")
    print("Carregando...")
    os.system("cls")
    print("FASE 01: Vamos testar sua sorte!")

    if teste_de_sorte():
        print("FASE: 02 ")
        












        
    else:
        print("Fim do jogo.")
