import turtle


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
controle_tabuleiro = [i for i in range(1, 10)]
for i in range(3):
    x = list()
    for j in range(3):
        x.append(False)
    tabuleiro.append(x)

print(tabuleiro)
print(controle_tabuleiro)

print("Clique na janela para terminar ...")
window.exitonclick()
