from random import randint # Importando biblioteca com função para escolha de número aleatóriamnte
from time import sleep # Importando biblioteca com função para retardar a resposta

# Ininio de Loop While para perguntas e respostas
while True:
    banca_aposta = randint(1,5) # Sorteio aleatório de número do programa
    jogador_escolhe = int(input('Escolha um número entre 1 até 5: ')) # Jogador escolhe um número para tentar a sorte
    if jogador_escolhe > 5 or jogador_escolhe < 1: # if para eliminar números que não estejam entre 1 a 5
        print('ERRADO - Número entre 1 até 5')
    elif jogador_escolhe == banca_aposta: # elif para caso de acerto do número escolhido pelo jogador
        print('Analisando dados que nem um funcionário de cartório...')
        sleep(2) # tempo de 2 seg para dar a resposta
        print('=' * 3, 'Acertou mizeravi!!!', '=' * 3)
        break # finaliza o programa quando o jogador acerta
    else: # else para caso de erro do número escolhido pelo jogador
        print('Analisando dados que nem um funcionário de cartório...')
        sleep(2)
        print(f'Errou jumento!!!, era {banca_aposta}')
        
