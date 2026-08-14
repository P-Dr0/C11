import numpy as np

matriz = np.zeros((2, 2))

linha_bomba = np.random.randint(0, 2)
coluna_bomba = np.random.randint(0, 2)
matriz[linha_bomba, coluna_bomba] = 1

jogadas = []
tentativas = 0

while tentativas < 3:
    linha = int(input("Escolha a linha (0 ou 1): "))
    coluna = int(input("Escolha a coluna (0 ou 1): "))

    if (linha, coluna) in jogadas:
        print("Posição já jogada, escolha outra.")
        continue

    jogadas.append((linha, coluna))
    tentativas += 1

    if matriz[linha, coluna] == 1:
        print("Game Over! :( Try Again!")
        break

    if len(jogadas) == 3:
        print("Congratulations! You beat the game! :)")
        break