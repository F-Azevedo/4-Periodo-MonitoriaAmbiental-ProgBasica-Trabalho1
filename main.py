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


def desenha_linha(t, inicio, fim):
    t.penup()
    t.setposition(inicio)
    t.pencolor('red')
    t.pendown()
    t.setposition(fim)
    t.penup()


def desenha_x(t, pos):
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


def desenha_o(t, pos):
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


def fim_de_jogo(t, tab, cont):
    # Verifica se tem um ganhador pelas linhas
    if tab[0][0] == tab[0][1] == tab[0][2] and (tab[0][0] == 'X' or tab[0][0] == 'O'):
        t.left(90)
        desenha_linha(t, (-225, 150), (225, 150))
        return tab[0][0]
    elif tab[1][0] == tab[1][1] == tab[1][2] and (tab[1][0] == 'X' or tab[1][0] == 'O'):
        t.left(90)
        desenha_linha(t, (-225, 0), (225, 0))
        return tab[1][0]
    elif tab[2][0] == tab[2][1] == tab[2][2] and (tab[2][0] == 'X' or tab[2][0] == 'O'):
        t.left(90)
        desenha_linha(t, (-225, -150), (225, -150))
        return tab[2][0]
    # Verifica se tem um ganhador pelas colunas
    elif tab[0][0] == tab[1][0] == tab[2][0] and (tab[0][0] == 'X' or tab[0][0] == 'O'):
        desenha_linha(t, (-150, 225), (-150, -225))
        return tab[0][0]
    elif tab[0][1] == tab[1][1] == tab[2][1] and (tab[0][1] == 'X' or tab[0][1] == 'O'):
        desenha_linha(t, (0, 225), (0, -225))
        return tab[0][1]
    elif tab[0][2] == tab[1][2] == tab[2][2] and (tab[0][2] == 'X' or tab[0][2] == 'O'):
        desenha_linha(t, (150, 225), (150, -225))
        return tab[0][2]
    # Verifica se tem um ganhador na diagonal principal
    elif tab[0][0] == tab[1][1] == tab[2][2] and (tab[0][0] == 'X' or tab[0][0] == 'O'):
        t.left(45)
        desenha_linha(t, (-225, 225), (225, -225))
        return tab[0][0]
    # Verifica se tem um ganhador na diagonal secundária
    elif tab[0][2] == tab[1][1] == tab[2][0] and (tab[0][2] == 'X' or tab[0][2] == 'O'):
        t.right(45)
        desenha_linha(t, (225, 225), (-225, -225))
        return tab[0][2]
    # Se não retornou ainda, significa que ninguem ganhou.
    # Verifica se já deu velha.
    elif cont == 9:
        return -1

    # Se ninguem ganhou e ainda tem espaços, continua o jogo
    return 0


def inicia_jogo(t, tab):
    jogador1 = True
    cont = 0
    ganhador = fim_de_jogo(t, tab, cont)
    while 0 == ganhador:
        pos = randint(0, 8)
        x = pos // 3
        y = pos % 3
        if tab[x][y] != 'X' and tab[x][y] != 'O':
            cont += 1
            if jogador1:
                tab[x][y] = 'X'
                desenha_x(t, pos)
                jogador1 = False
            else:
                tab[x][y] = 'O'
                desenha_o(t, pos)
                jogador1 = True
        ganhador = fim_de_jogo(t, tab, cont)


# Inicialização da Tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape('turtle')
tartaruga.speed('fast')

# Definição do tamanho da tela
turtle.screensize(450, 450)
largura, altura = turtle.screensize()

# Estilização da tela
window = turtle.Screen()
tartaruga.pensize(5)
window.bgcolor('light cyan')
window.setup(1.2 * largura, 1.2 * altura)

# Cria o tabuleiro do jogo
cria_tabuleiro(tartaruga, largura, altura)

# Inicia variáveis para controle do tabuleiro
tabuleiro = list()
for i in range(3):
    aux = list()
    for j in range(3):
        aux.append(False)
    tabuleiro.append(aux)

inicia_jogo(tartaruga, tabuleiro)

print("Clique na janela para terminar ...")
window.exitonclick()
