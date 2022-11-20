# Importação de bibliotecas externa
from math import *
import matplotlib.pyplot as plt
from tkinter import *
from random import uniform
from os import system, name
from time import sleep

X_ROBO = 0 #(m)
Y_ROBO = 0 #(m)
PONTO_INICIAL = [] #X[0] e Y[1] (m)
RAIO_INTERCEPTACAO = 0.111335 #(m)
VELOCIDADE_ROBO = 2.8 #Módulo da velocidade do robô
ACELERACAO_ROBO = 2.8 #Módulo da aceleração do robô
VELOCIDADE_ROBO_X = 0 #Decomposição da velocidade do robô no eixo X
VELOCIDADE_ROBO_Y = 0 #Decomposição da velocidade do robô no eixo Y
ACELERACAO_ROBO_X = 0 #Decomposição da aceleração do robô no eixo X
ACELERACAO_ROBO_Y = 0 #Decomposição da aceleração do robô no eixo Y
velocidade_instantanea_BOLA_X = []
velocidade_instantanea_BOLA_Y = []
velocidade_instantanea_ROBO_X = []
velocidade_instantanea_ROBO_Y = []
trajetoria_x_BOLA = [] #Todos os pontos da trajetória da bola em X
trajetoria_y_BOLA = [] #Todos os pontos da trajetória da bola em Y
tempo_bola = [] #Todos os tempos da bola
trajetoria_X_ROBO = [] #Todos os pontos da trajetória do robõ em X
trajetoria_Y_ROBO = [] #Todos os pontos da trajetória do robô em Y
tempo_robo_trajetoria = [] #Todos os tempos em que o robô chega aos pontos da trajetória
lista_aceleracao_ROBO_x = []
lista_aceleracao_ROBO_y = []
lista_aceleracao_BOLA_x = []
lista_aceleracao_BOLA_y = []
ponto_interceptacao = []  #X[0] e Y[1] (m)
tempo_interceptacao = 0
modulo_distancia_relativa = []
index_tempo_interceptacao = 0

#=============================================================================================================================================================#
# F R O N T E N D

# Declara janela principal
janela_principal = Tk()
# Adiciona título a página principal
janela_principal.title('Projeto Futebol de Robôs')
# Define tamanho e características da janela
janela_principal.geometry("415x465")
janela_principal.resizable(False, False)
janela_principal.configure(background='#2d2d2d')
janela_principal.iconbitmap('img/soccer-ball.ico')

# Área para inserir coordenadas do robô
x_robo = Label(janela_principal, text = "Coordenada X do robô", width = 20).place(x = 38, y = 30) 
y_robo = Label(janela_principal, text = "Coordenada Y do robô", width = 20).place(x = 38, y = 70) 
raio_interceptacao = Label(janela_principal, text = "Raio de interceptação", width = 20).place(x = 38, y = 110) 
x_robo_input = Entry(janela_principal, width = 31)
x_robo_input.place(x = 198, y = 30)
y_robo_input = Entry(janela_principal, width = 31)
y_robo_input.place(x = 198, y = 70)
raio_interceptacao_input = Entry(janela_principal, width = 31)
raio_interceptacao_input.place(x = 198, y = 110)

#=============================================================================================================================================================#

def get_params():
    global X_ROBO, Y_ROBO, RAIO_INTERCEPTACAO, ponto_interceptacao
    if x_robo_input.get() != "" and y_robo_input.get() != "":
        X_ROBO = float(x_robo_input.get())
        Y_ROBO = float(y_robo_input.get())
    else:
        v = True
        randX = 0
        randY = 0
        while (v):
            randX = float(uniform(0, 1))
            randY = float(uniform(0, 1))
            d = sqrt((1 - randX) ** 2 + (0.700 - randY) ** 2)
            if d < 1.22 and randX != 1 and randY != 0.700:
                v = False
        X_ROBO = randX
        Y_ROBO = randY
    
    if raio_interceptacao_input.get() != "":
        RAIO_INTERCEPTACAO = float(raio_interceptacao_input.get())
    else:
        RAIO_INTERCEPTACAO = 0.111335

def reset_variables():

    global X_ROBO, Y_ROBO, PONTO_INICIAL, RAIO_INTERCEPTACAO, VELOCIDADE_ROBO, ACELERACAO_ROBO, VELOCIDADE_ROBO_X, VELOCIDADE_ROBO_Y,ACELERACAO_ROBO_X, ACELERACAO_ROBO_Y, velocidade_instantanea_BOLA_X, velocidade_instantanea_BOLA_Y, velocidade_instantanea_ROBO_X, velocidade_instantanea_ROBO_Y, trajetoria_x_BOLA, trajetoria_y_BOLA, tempo_bola, trajetoria_X_ROBO, trajetoria_Y_ROBO, tempo_robo_trajetoria, lista_aceleracao_ROBO_x, lista_aceleracao_ROBO_y, lista_aceleracao_BOLA_x, lista_aceleracao_BOLA_y, ponto_interceptacao, tempo_interceptacao, modulo_distancia_relativa, index_tempo_interceptacao

    #Redefinição das variáveis para reiniciar o código. ->
    X_ROBO = 0 #(m)
    Y_ROBO = 0 #(m)
    PONTO_INICIAL = [] #X[0] e Y[1] (m)
    RAIO_INTERCEPTACAO = 0.111335 #(m)
    VELOCIDADE_ROBO = 2.8 #Módulo da velocidade do robô
    ACELERACAO_ROBO = 2.8 #Módulo da aceleração do robô
    VELOCIDADE_ROBO_X = 0 #Decomposição da velocidade do robô no eixo X
    VELOCIDADE_ROBO_Y = 0 #Decomposição da velocidade do robô no eixo Y
    velocidade_instantanea_BOLA_X = []
    velocidade_instantanea_BOLA_Y = []
    velocidade_instantanea_ROBO_X = []
    velocidade_instantanea_ROBO_Y = []
    trajetoria_x_BOLA = [] #Todos os pontos da trajetória da bola em X
    trajetoria_y_BOLA = [] #Todos os pontos da trajetória da bola em Y
    tempo_bola = [] #Todos os tempos da bola
    trajetoria_X_ROBO = [] #Todos os pontos da trajetória do robõ em X
    trajetoria_Y_ROBO = [] #Todos os pontos da trajetória do robô em Y
    tempo_robo_trajetoria = [] #Todos os tempos em que o robô chega aos pontos da trajetória
    ACELERACAO_ROBO_X = 0 #Decomposição da aceleração do robô no eixo X
    ACELERACAO_ROBO_Y = 0 #Decomposição da aceleração do robô no eixo Y
    lista_aceleracao_ROBO_x = []
    lista_aceleracao_ROBO_y = []
    lista_aceleracao_BOLA_x = []
    lista_aceleracao_BOLA_y = []
    ponto_interceptacao = []  #X[0] e Y[1] (m)
    tempo_interceptacao = 0
    modulo_distancia_relativa = []
    index_tempo_interceptacao = 0

def execute():
    reset_variables()
    get_params()

    # Ponto inicial robô em X
    PONTO_INICIAL.append(float(X_ROBO))
    # Ponto inicial robô em Y
    PONTO_INICIAL.append(float(Y_ROBO))

    # Leitura de arquivo com pontos da trajetória da bola
    with open("trajetoria_bola_noturno.txt", "r") as file:
        file = file.readlines()
        for i in file:
            # Manipulação de arquivo (Desmembramento do arquivo em listas de informações)
            tempo_bola.append(float(i.split("\t")[0]))
            trajetoria_x_BOLA.append(float(i.split("\t")[1]))
            trajetoria_y_BOLA.append(float(i.split("\t")[2]))

            # Variáveis declaradas para cálculos locais
            x_bola = float(i.split("\t")[1])
            y_bola = float(i.split("\t")[2])

            # Fórmula da distância do robô até cada ponto da trajetória da bola
            distancia = sqrt((x_bola-X_ROBO)**2+(y_bola-Y_ROBO)** 2) - float(RAIO_INTERCEPTACAO)

            # Declaração de variável para cálculo locai
            tempo_total = 0

            # Verificação para ver se o robô atinge a velocidade máxima durante a trajetória
            if distancia <= 1.4:
                tempo_total = sqrt((distancia*2)/ACELERACAO_ROBO)
            else:
                tempo_velocidade_maxima = sqrt((1.4*2)/ACELERACAO_ROBO)
                tempo_velocidade_constante = (distancia - 1.4) / VELOCIDADE_ROBO
                tempo_total = tempo_velocidade_constante + tempo_velocidade_maxima

            # Adiciona em uma lista todos os tempos para alcançar cada ponto
            tempo_robo_trajetoria.append(round(tempo_total, 2))

    # O codigo abaixo obtem o menor tempo que o robo leva para encontrar a bola
    # no qual o menor_tempo_bola será o menor tempo.
    count = 0  # Variável contador local
    for i in range(0, len(tempo_bola)+1, 1):
        # Condicional responsável por pegar menores tempos de interceptação
        if (float(tempo_robo_trajetoria[i]) - float(tempo_bola[i])) <= 0.03:
            menor_tempo_bola = tempo_bola[i]
            count = i
            break
    ponto_interceptacao.append(trajetoria_x_BOLA[count])
    ponto_interceptacao.append(trajetoria_y_BOLA[count])

    verficadorX = float(ponto_interceptacao[0]) - float(PONTO_INICIAL[0])
    verficadorY = float(ponto_interceptacao[1]) - float(PONTO_INICIAL[1])

    # Calculo da angulação do robo em relação aos eixos
    coef_angular = verficadorY / verficadorX

    # Variáveis, funções e cálculos utilizados para geração de todos os gráficos
    arco = atan(coef_angular)
    cos_arc = cos(arco)
    sin_arc = sin(arco)
    if (verficadorX < 0):
        cos_arc = cos_arc * -1
    if (verficadorX < 0 and verficadorY > 0 or verficadorX < 0 and verficadorY < 0):
        sin_arc = sin_arc * -1

    ACELERACAO_ROBO_X = ACELERACAO_ROBO*cos_arc
    VELOCIDADE_ROBO_X = VELOCIDADE_ROBO*cos_arc
    ACELERACAO_ROBO_Y = ACELERACAO_ROBO*sin_arc 
    VELOCIDADE_ROBO_Y = VELOCIDADE_ROBO*sin_arc

    trajetoria_X_ROBO_ANTES_VEL_MAX = []
    trajetoria_X_ROBO_DEPOIS_VEL_MAX = []
    trajetoria_Y_ROBO_ANTES_VEL_MAX = []
    trajetoria_Y_ROBO_DEPOIS_VEL_MAX = []
    VELOCIDADE_CONSTANTE_X = []
    VELOCIDADE_CONSTANTE_Y = []
    global index_tempo_interceptacao
    index_tempo_interceptacao = tempo_bola.index(menor_tempo_bola)
#=============================================================================================================================================================#
    for i in tempo_bola:
        vel_bola_x_inst = -0.021 *(i**2) + (0.34*i) + 2.5
        vel_bola_y_inst = (-0.4*i) + 1.8
        velocidade_instantanea_BOLA_X.append(vel_bola_x_inst)
        velocidade_instantanea_BOLA_Y.append(vel_bola_y_inst)
        if i < 1:
            vel_instantanea = 2.8 * i
            velocidade_instantanea_ROBO_X.append(vel_instantanea*cos_arc)
            velocidade_instantanea_ROBO_Y.append(vel_instantanea*sin_arc)
        else:
            VELOCIDADE_CONSTANTE_X.append(2.8*cos_arc)
            VELOCIDADE_CONSTANTE_Y.append(2.8*sin_arc)
#=============================================================================================================================================================#
        if float(i) <= float(menor_tempo_bola):
            # Velocidade Variada
            if (float(i) <= 1):
                x_robo_var = float(PONTO_INICIAL[0]) + (ACELERACAO_ROBO_X * (float(i)**2)) / 2
                trajetoria_X_ROBO_ANTES_VEL_MAX.append(x_robo_var)
                y_robo_var = float(PONTO_INICIAL[1]) + (ACELERACAO_ROBO_Y * (float(i)**2)) / 2
                trajetoria_Y_ROBO_ANTES_VEL_MAX.append(y_robo_var)
            # Velocidade Constante
            else:
                x_robo_const = float(trajetoria_X_ROBO_ANTES_VEL_MAX[-1]) + VELOCIDADE_ROBO_X * (float(i)-1)
                trajetoria_X_ROBO_DEPOIS_VEL_MAX.append(x_robo_const)
                y_robo_const = float(trajetoria_Y_ROBO_ANTES_VEL_MAX[-1]) + VELOCIDADE_ROBO_Y * (float(i)-1)
                trajetoria_Y_ROBO_DEPOIS_VEL_MAX.append(y_robo_const)
#=============================================================================================================================================================#
    # Loops responsáveis por juntar as listas criadas:
    #Posições do Robô em X
    for i in trajetoria_X_ROBO_ANTES_VEL_MAX:
        trajetoria_X_ROBO.append(float(i))
    for i in trajetoria_X_ROBO_DEPOIS_VEL_MAX:
        trajetoria_X_ROBO.append(float(i))

    #Posições do Robô em Y
    for i in trajetoria_Y_ROBO_ANTES_VEL_MAX:
        trajetoria_Y_ROBO.append(float(i))
    for i in trajetoria_Y_ROBO_DEPOIS_VEL_MAX:
        trajetoria_Y_ROBO.append(float(i))

    #Velocidades do Robô
    for i in VELOCIDADE_CONSTANTE_X:
       velocidade_instantanea_ROBO_X.append(i)
    for i in VELOCIDADE_CONSTANTE_Y:
       velocidade_instantanea_ROBO_Y.append(i)

    #Aceleração do Robô
    for i in trajetoria_X_ROBO:
        lista_aceleracao_ROBO_x.append(ACELERACAO_ROBO_X)
    for i in trajetoria_Y_ROBO:
        lista_aceleracao_ROBO_y.append(ACELERACAO_ROBO_Y)

    #Aceleração da Bola
    for i in tempo_bola[0:index_tempo_interceptacao]:
        lista_aceleracao_BOLA_x.append((-0.042*i)-0.34)
    for i in tempo_bola[0:index_tempo_interceptacao]:
        lista_aceleracao_BOLA_y.append(-0.4)

    #Distancia Relativa
    for i in range(len(trajetoria_X_ROBO)):
        modulo = sqrt( (float(ponto_interceptacao[0]) - trajetoria_X_ROBO[i])**2 + (float(ponto_interceptacao[1]) - trajetoria_Y_ROBO[i])**2) - RAIO_INTERCEPTACAO
        modulo_distancia_relativa.append(modulo)

#=============================================================================================================================================================#
    #OUTPUTS DO TERMINAL#
    sleep(1)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("Ponto inicial: (%.2f, %.2f)" %(X_ROBO, Y_ROBO))
    print("\nO tempo de interceptação é de %.2f segundos." %menor_tempo_bola)
    print("\nPonto de interceptação: ", end="")
    print("P(%s, %s)" %(ponto_interceptacao[0], ponto_interceptacao[1]))
    print("\nVelocidade Final em X do Robô: %.3f m/s²" %velocidade_instantanea_ROBO_X[index_tempo_interceptacao])
    print("\nVelocidade Final em Y do Robô: %.3f m/s²" %velocidade_instantanea_ROBO_Y[index_tempo_interceptacao])
    print("\nVelocidade Final em X da Bola: %.3f m/s²" %velocidade_instantanea_BOLA_X[index_tempo_interceptacao])
    print("\nVelocidade Final em Y da Bola: %.3f m/s²" %velocidade_instantanea_BOLA_Y[index_tempo_interceptacao])

# A partir desse ponto do algoritmo os gráficos serão gerados.
#=============================================================================================================================================================#
# Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦, até o ponto de interceptação

def graphic1():
    plt.plot([float(ponto_interceptacao[0]), X_ROBO], [float(ponto_interceptacao[1]), Y_ROBO], linestyle='dotted', marker='o', color='red', markersize=3)
    plt.plot(trajetoria_x_BOLA[0:trajetoria_x_BOLA.index(float(ponto_interceptacao[0]))], trajetoria_y_BOLA[0:trajetoria_y_BOLA.index(float(ponto_interceptacao[1]))], linestyle='dotted')
    plt.ylabel("Y (m)")
    plt.xlabel("X (m)")
    plt.title("Gráfico de X em função de Y da interceptação")
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    plt.yticks([0, 1, 2, 3, 4, 5, 6])
    plt.legend(["Robô", "Bola"], loc="lower right")
    plt.show()
#=============================================================================================================================================================#
# Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡 até o instante de interceptação;

def graphic2_X():
    plt.plot(tempo_bola[0:len(trajetoria_X_ROBO)], trajetoria_X_ROBO)
    plt.plot(tempo_bola[0:trajetoria_x_BOLA.index(float(ponto_interceptacao[0]))], trajetoria_x_BOLA[0:trajetoria_x_BOLA.index(float(ponto_interceptacao[0]))])
    plt.ylabel("X (m)")
    plt.xlabel("t (s)")
    plt.title("Gráfico de X em função do tempo da interceptação")
    plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9])
    plt.xticks([0, 1, 2, 3, 4])
    plt.legend(["Robô", "Bola"], loc="lower right")
    plt.show()

def graphic2_Y():
    plt.plot(tempo_bola[0:len(trajetoria_Y_ROBO)], trajetoria_Y_ROBO)
    plt.plot(tempo_bola[0:trajetoria_y_BOLA.index(float(ponto_interceptacao[1]))], trajetoria_y_BOLA[0:trajetoria_y_BOLA.index(float(ponto_interceptacao[1]))])
    plt.ylabel("Y (m)")
    plt.xlabel("t (s)")
    plt.title("Gráfico de Y em função do tempo da interceptação")
    plt.legend(["Robô", "Bola"], loc="lower right")
    plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
    plt.xticks([0, 1, 2, 3, 4])
    plt.show()

def graphic2_overall():
    graphic2_X()
    graphic2_Y()
#=============================================================================================================================================================#
# Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡 até o instante de interceptação;

def graphic3_X():
    plt.plot(tempo_bola[0:index_tempo_interceptacao], velocidade_instantanea_ROBO_X[0:index_tempo_interceptacao])
    plt.plot(tempo_bola[0:index_tempo_interceptacao], velocidade_instantanea_BOLA_X[0:index_tempo_interceptacao])
    plt.ylabel("Vx (m/s)")
    plt.xlabel("t (s)")
    plt.title("Gráfico da velocidade em X em função do tempo da interceptação")
    plt.legend(["Robô", "Bola"], loc="lower right")
    plt.yticks([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])
    plt.xticks([0, 1, 2, 3, 4])
    plt.show()

def graphic3_Y():
    plt.plot(tempo_bola[0:index_tempo_interceptacao], velocidade_instantanea_ROBO_Y[0:index_tempo_interceptacao])
    plt.plot(tempo_bola[0:index_tempo_interceptacao], velocidade_instantanea_BOLA_Y[0:index_tempo_interceptacao])
    plt.ylabel("Vy (m/s)")
    plt.xlabel("t (s)")
    plt.title("Gráfico da velocidade em Y em função do tempo até a interceptação")
    plt.legend(["Robô", "Bola"], loc="lower right")
    plt.yticks([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5])
    plt.xticks([0, 1, 2, 3, 4])
    plt.show()

def graphic3_overall():
    graphic3_X()
    graphic3_Y()
#=============================================================================================================================================================#
#Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo 𝑡 até o instante de interceptação;

def graphic4_X():
    plt.plot(tempo_bola[0:len(lista_aceleracao_ROBO_x)], lista_aceleracao_ROBO_x)
    plt.plot(tempo_bola[0:index_tempo_interceptacao], lista_aceleracao_BOLA_x[0:index_tempo_interceptacao])

    plt.ylabel("Ax (m/s)^2")
    plt.xlabel("t (s)")
    plt.title("Gráfico da aceleração em X em função do tempo até a interceptação")
    plt.legend(["Robô", "Bola"], loc="lower right")
    plt.yticks([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5])
    plt.xticks([0, 1, 2, 3, 4])
    plt.show()

def graphic4_Y():
    plt.plot(tempo_bola[0:len(lista_aceleracao_ROBO_y)], lista_aceleracao_ROBO_y)
    plt.plot(tempo_bola[0:index_tempo_interceptacao], lista_aceleracao_BOLA_y[0:index_tempo_interceptacao])

    plt.ylabel("Ay (m/s)^2")
    plt.xlabel("t (s)")
    plt.title("Gráfico da aceleração em Y em função do tempo até a interceptação")
    plt.legend(["Robô", "Bola"], loc="lower right")
    plt.yticks([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5])
    plt.xticks([0, 1, 2, 3, 4])
    plt.show()

def graphic4_overall():
    graphic4_X()
    graphic4_Y()
#=============================================================================================================================================================#
# Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡 até o instante de interceptação;

def graphic5():
    plt.plot(tempo_bola[0:index_tempo_interceptacao], modulo_distancia_relativa[0:index_tempo_interceptacao])
    plt.ylabel("d (m)")
    plt.xlabel("t (s)")
    plt.title("Gráfico da distância relativa d entre o robô e a bola em função do tempo")
    plt.legend(["Distância"], loc="lower right")
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    plt.xticks([0, 1, 2, 3, 4])
    plt.show()
#=============================================================================================================================================================#
input_cordenadas = Button(janela_principal, text = "Enviar", fg='white', bg='#0e8ed4', cursor='mouse', width = 20, command=execute).place(x = 38, y = 150)
warning = Label(janela_principal, text = "*Insira apenas números", bg='#2d2d2d', fg='red').place(x = 190, y = 152) 
gerar = Button(janela_principal, text = "Gráfico das trajetórias", fg='white', bg='#0e8ed4', cursor='mouse', width = 50, command=graphic1).place(x = 25, y = 210)
gerar_1 = Button(janela_principal, text = "Gráfico das coordenadas em função do tempo", fg='white', bg='#0e8ed4', cursor='mouse', width = 50, height = 1, command=graphic2_overall).place(x = 25, y = 260)
gerar_2 = Button(janela_principal, text = "Gráfico das velocidades em função do tempo", fg='white', bg='#0e8ed4', cursor='mouse', width = 50, command=graphic3_overall).place(x = 25, y = 310)
gerar_3 = Button(janela_principal, text = "Gráfico das acelerações em função do tempo", fg='white', bg='#0e8ed4', cursor='mouse', width = 50, command=graphic4_overall).place(x = 25, y = 360)
gerar_4 = Button(janela_principal, text = "Gráfico da distância relativa em função do tempo", fg='white', bg='#0e8ed4', cursor='mouse', width = 50, command=graphic5).place(x = 25, y = 410)
janela_principal.mainloop()
#=============================================================================================================================================================#