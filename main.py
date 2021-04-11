import turtle
from random import randint


def cria_tabuleiro(t, w, h):
    # Primeira Linha
    t.penup()
    primeira_linha = h/2 - h/3
    # print(primeira_linha)
    t.setposition(-h/2, primeira_linha)
    t.pendown()
    t.forward(w)
    t.penup()

    # Segunda Linha
    segunda_linha = h/3 - h/2
    # print(segunda_linha)
    t.setposition(-h/2, segunda_linha)
    t.pendown()
    t.forward(w)
    t.penup()

    t.right(90)

    # Primeira Coluna
    primeira_coluna = w/2 - w/3
    # print(primeira_coluna)
    t.setposition(primeira_coluna, h/2)
    t.pendown()
    t.forward(h)
    t.penup()

    # Segunda Coluna
    segunda_coluna = w/3 - w/2
    # print(segunda_coluna)
    t.setposition(segunda_coluna, h/2)
    t.pendown()
    t.forward(h)
    t.penup()


def desenha_x(t, w, h, pos):
    if pos == 0:
        t.penup()
        t.setposition(-150, 150)
        t.pendown()
        t.setposition(-150 + 25, 150 + 25)
        t.setposition(-150, 150)
        t.setposition(-150 + 25, 150 - 25)
        t.setposition(-150, 150)
        t.setposition(-150 - 25, 150 - 25)
        t.setposition(-150, 150)
        t.setposition(-150 - 25, 150 + 25)
        t.penup()
    elif pos == 1:
        t.penup()
        t.setposition(0, 150)
        t.pendown()
        t.setposition(0 + 25, 150 + 25)
        t.setposition(0, 150)
        t.setposition(0 + 25, 150 - 25)
        t.setposition(0, 150)
        t.setposition(0 - 25, 150 - 25)
        t.setposition(0, 150)
        t.setposition(0 - 25, 150 + 25)
        t.penup()
    elif pos == 2:
        t.penup()
        t.setposition(150, 150)
        t.pendown()
        t.setposition(150 + 25, 150 + 25)
        t.setposition(150, 150)
        t.setposition(150 + 25, 150 - 25)
        t.setposition(150, 150)
        t.setposition(150 - 25, 150 - 25)
        t.setposition(150, 150)
        t.setposition(150 - 25, 150 + 25)
        t.penup()
    elif pos == 3:
        t.penup()
        t.setposition(-150, 0)
        t.pendown()
        t.setposition(-150 + 25, 0 + 25)
        t.setposition(-150, 0)
        t.setposition(-150 + 25, 0 - 25)
        t.setposition(-150, 0)
        t.setposition(-150 - 25, 0 - 25)
        t.setposition(-150, 0)
        t.setposition(-150 - 25, 0 + 25)
        t.penup()
    elif pos == 4:
        t.penup()
        t.setposition(0, 0)
        t.pendown()
        t.setposition(0 + 25, 0 + 25)
        t.setposition(0, 0)
        t.setposition(0 + 25, 0 - 25)
        t.setposition(0, 0)
        t.setposition(0 - 25, 0 - 25)
        t.setposition(0, 0)
        t.setposition(0 - 25, 0 + 25)
        t.penup()
    elif pos == 5:
        t.penup()
        t.setposition(150, 0)
        t.pendown()
        t.setposition(150 + 25, 0 + 25)
        t.setposition(150, 0)
        t.setposition(150 + 25, 0 - 25)
        t.setposition(150, 0)
        t.setposition(150 - 25, 0 - 25)
        t.setposition(150, 0)
        t.setposition(150 - 25, 0 + 25)
        t.penup()
    elif pos == 6:
        t.penup()
        t.setposition(-150, -150)
        t.pendown()
        t.setposition(-150 + 25, -150 + 25)
        t.setposition(-150, -150)
        t.setposition(-150 + 25, -150 - 25)
        t.setposition(-150, -150)
        t.setposition(-150 - 25, -150 - 25)
        t.setposition(-150, -150)
        t.setposition(-150 - 25, -150 + 25)
        t.penup()
    elif pos == 7:
        t.penup()
        t.setposition(0, -150)
        t.pendown()
        t.setposition(0 + 25, -150 + 25)
        t.setposition(0, -150)
        t.setposition(0 + 25, -150 - 25)
        t.setposition(0, -150)
        t.setposition(0 - 25, -150 - 25)
        t.setposition(0, -150)
        t.setposition(0 - 25, -150 + 25)
        t.penup()
    elif pos == 8:
        t.penup()
        t.setposition(150, -150)
        t.pendown()
        t.setposition(150 + 25, -150 + 25)
        t.setposition(150, -150)
        t.setposition(150 + 25, -150 - 25)
        t.setposition(150, -150)
        t.setposition(150 - 25, -150 - 25)
        t.setposition(150, -150)
        t.setposition(150 - 25, -150 + 25)
        t.penup()


def desenha_o(t, w, h, pos):
    if pos == 0:
        t.setposition(-200, 150)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 1:
        t.setposition(-50, 150)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 2:
        t.setposition(100, 150)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 3:
        t.setposition(-200, 0)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 4:
        t.setposition(-50, 0)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 5:
        t.setposition(100, 0)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 6:
        t.setposition(-200, -150)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 7:
        t.setposition(-50, -150)
        t.pendown()
        t.circle(50)
        t.penup()
    elif pos == 8:
        t.setposition(100, -150)
        t.pendown()
        t.circle(50)
        t.penup()


def fim_de_jogo(tabuleiro, controle_tabuleiro):
    # Verifica se tem um ganhador pelas linhas
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and (tabuleiro[0][0] == 'X' or tabuleiro[0][0] == 'O'):
        return tabuleiro[0][0]
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and (tabuleiro[1][0] == 'X' or tabuleiro[1][0] == 'O'):
        return tabuleiro[1][0]
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and (tabuleiro[2][0] == 'X' or tabuleiro[2][0] == 'O'):
        return tabuleiro[2][0]
    # Verifica se tem um ganhador pelas colunas
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and (tabuleiro[0][0] == 'X' or tabuleiro[0][0] == 'O'):
        return tabuleiro[0][0]
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and (tabuleiro[0][1] == 'X' or tabuleiro[0][1] == 'O'):
        return tabuleiro[0][1]
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and (tabuleiro[0][2] == 'X' or tabuleiro[0][2] == 'O'):
        return tabuleiro[0][2]
    # Verifica se tem um ganhador na diagonal principal
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and (tabuleiro[0][0] == 'X' or tabuleiro[0][0] == 'O'):
        return tabuleiro[0][0]
    # Verifica se tem um ganhador na diagonal secundária
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and (tabuleiro[0][2] == 'X' or tabuleiro[0][2] == 'O'):
        return tabuleiro[0][2]
    # Se não retornou ainda, significa que ninguem ganhou.
    # Verifica se já deu velha.
    elif len(controle_tabuleiro) == 0:
        return -1

    # Se ninguem ganhou e ainda tem espaços, continua o jogo
    return 0


def inicia_jogo(t, tabuleiro, controle_tabuleiro, w, h):
    jogador1 = True
    ganhador = fim_de_jogo(tabuleiro, controle_tabuleiro)
    while 0 == ganhador:
        pos = randint(0, 8)
        if pos in controle_tabuleiro:
            controle_tabuleiro.remove(pos)
            x = pos // 3
            y = pos % 3
            print(f"Número selecionado {pos}, num//3 = {pos//3}, num%3 = {pos%3}\n", flush=True)
            if jogador1:
                tabuleiro[x][y] = 'X'
                desenha_x(t, w, h, pos)
                jogador1 = False
            else:
                tabuleiro[x][y] = 'O'
                desenha_o(t, w, h, pos)
                jogador1 = True
        ganhador = fim_de_jogo(tabuleiro, controle_tabuleiro)
    print(f"Tabuleiro: {tabuleiro}")
    print(f"Controle: {controle_tabuleiro}")
    print(f"Ganhador: {ganhador}")


# Inicialização da Tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape('turtle')
tartaruga.speed('fast')
print(f"Estou na posição {tartaruga.pos()}")
print(f"Em relação à horizontal o meu ângulo é {tartaruga.heading()} graus.")

# Definição do tamanho da tela
turtle.screensize(450, 450)
w, h = turtle.screensize()
print(f"largura = {w} altura = {h}")

# Estilização da tela
window = turtle.Screen()
tartaruga.pensize(5)
window.bgcolor('light cyan')
window.setup(1.2*w, 1.2*h)

# Cria o tabuleiro do jogo
cria_tabuleiro(tartaruga, w, h)

# Inicia variáveis para controle do tabuleiro
tabuleiro = list()
controle_tabuleiro = [i for i in range(0, 9)]
for i in range(3):
    x = list()
    for j in range(3):
        x.append(False)
    tabuleiro.append(x)

print(tabuleiro)
print(controle_tabuleiro)

tartaruga.speed('slowest')
inicia_jogo(tartaruga, tabuleiro, controle_tabuleiro, w, h)

print("Clique na janela para terminar ...")
window.exitonclick()
