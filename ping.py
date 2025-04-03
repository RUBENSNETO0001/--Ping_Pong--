import turtle

# Configurações da tela
tela = turtle.Screen()
tela.title("Ping Pong")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# Pontuação
pontuacao_a = 0
pontuacao_b = 0

# Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=6, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=6, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(10)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.4
bola.dy = 0.4

# Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador A: 0  Jogador B: 0", align="center", font=("Courier", 24, "normal"))

# Funções de movimentação
def mover_raquete_a_cima():
    y = raquete_a.ycor()
    if y < 250:
        raquete_a.sety(y + 20)

def mover_raquete_a_baixo():
    y = raquete_a.ycor()
    if y > -240:
        raquete_a.sety(y - 20)

def mover_raquete_b_cima():
    y = raquete_b.ycor()
    if y < 250:
        raquete_b.sety(y + 20)

def mover_raquete_b_baixo():
    y = raquete_b.ycor()
    if y > -240:
        raquete_b.sety(y - 20)

# Teclado
tela.listen()
tela.onkeypress(mover_raquete_a_cima, "w")
tela.onkeypress(mover_raquete_a_baixo, "s")
tela.onkeypress(mover_raquete_b_cima, "Up")
tela.onkeypress(mover_raquete_b_baixo, "Down")

# Loop principal
enquanto = True
while enquanto:
    tela.update()

    # Movimentação da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Colisões com a borda superior e inferior
    if bola.ycor() > 290 or bola.ycor() < -290:
        bola.dy *= -1

    # Colisões com as raquetes
    if (bola.xcor() > 340 and bola.xcor() < 350) and (raquete_b.ycor() - 50 < bola.ycor() < raquete_b.ycor() + 50):
        bola.setx(340)
        bola.dx *= -1
    elif (bola.xcor() < -340 and bola.xcor() > -350) and (raquete_a.ycor() - 50 < bola.ycor() < raquete_a.ycor() + 50):
        bola.setx(-340)
        bola.dx *= -1

    # Pontuação
    if bola.xcor() > 390:
        pontuacao_a += 1
        bola.goto(0, 0)
        bola.dx *= -1
        placar.clear()
        placar.write(f"Jogador A: {pontuacao_a}  Jogador B: {pontuacao_b}", align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        pontuacao_b += 1
        bola.goto(0, 0)
        bola.dx *= -1
        placar.clear()
        placar.write(f"Jogador A: {pontuacao_a}  Jogador B: {pontuacao_b}", align="center", font=("Courier", 24, "normal"))
