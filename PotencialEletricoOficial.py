# Trabalho de Física - Potencial Elétrico
# Alberth Emanuel - Carolina Fonseca - Raissa Maia

#Extensões que serão usadas são: matplotlib, numpy e tkinter
import tkinter as tk
from tkinter import simpledialog

import matplotlib.pyplot as plt
import numpy as np

fig = None


# Função para selecionar a quantidade de cargas elétricas
def selecionar_quantidade_cargas():
    
     # Cria uma janela pop-up usando tkinter e pede ao usuário para selecionar a quantidade de cargas
    root = tk.Tk()
    root.withdraw()
    
    num_cargas = simpledialog.askinteger("Quantidade de Cargas", "Selecione a quantidade de cargas elétricas (1 a 4):", minvalue=1, maxvalue=4)
    root.destroy()
    
    return num_cargas


# Função para selecionar os valores das cargas elétricas e suas posições    
def selecionar_valores_cargas(num_cargas):
    
    cargas = []
    root = tk.Tk()
    root.withdraw()
    
    for i in range(num_cargas):
        
        carga = simpledialog.askfloat(f"Carga {i+1}", f"Digite a carga {i+1} (em Coulombs):")
        pos_x = simpledialog.askfloat(f"Carga {i+1}", f"Digite a posição x da carga {i+1}:")
        pos_y = simpledialog.askfloat(f"Carga {i+1}", f"Digite a posição y da carga {i+1}:")
        
        cargas.append((carga, (pos_x, pos_y)))
        
    root.destroy()
    return cargas


# Função para calcular o potencial elétrico em um ponto causado por uma carga em uma posição   
def calcular_potencial(carga, pos_carga, ponto):
    
    k = 9e9 # Constante eletrostática (k)
    
    # Cálculo da distância entre a carga e o ponto no espaço
    dx = ponto[0] - pos_carga[0]
    dy = ponto[1] - pos_carga[1]
    distancia = (dx**2 + dy**2)**0.5
    
    return k * carga / distancia    # Cálculo do potencial elétrico usando a Lei de Coulomb

# ************************************************************************************************

# Função para criar o gráfico de contorno do potencial elétrico usando  
def criar_grafico_contorno(cargas, resolucao = 100):
    
    # Definição das coordenadas do espaço em que o gráfico será criado
    x_min, x_max = -10, 10
    y_min, y_max = -10, 10
    
    x = np.linspace(x_min, x_max, resolucao)
    y = np.linspace(y_min, y_max, resolucao)
    
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    # Cálculo do potencial elétrico em cada ponto do espaço e armazenamento nos valores de Z
    for i in range(resolucao):
        
        for j in range(resolucao):
            ponto = (X[i, j], Y[i, j])
            
            for carga, pos_carga in cargas:
                Z[i, j] += calcular_potencial(carga, pos_carga, ponto)

    return X, Y, Z


# Função para desenhar as cargas no gráfico e criar os subplots para os gráficos       
def desenhar_grafico_cargas(cargas):
    
    global fig  
    
    # Criação da figura e dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Desenho das cargas elétricas no primeiro subplot (gráfico 2D)
    for carga, pos in cargas:
        ax1.scatter(pos[0], pos[1], s=100, label=f"Carga: {carga}")

    ax1.set_xlabel('Eixo x')
    ax1.set_ylabel('Eixo y')
    ax1.legend()

    # Modo interativo
    plt.ion()
    plt.show()

    return ax1, ax2


# Função para atualizar o gráfico de contorno           
def atualizar_grafico_contorno(ax2, X, Y, Z, valores_cargas, ponto):        
    
    # Recálculo do potencial elétrico em cada ponto do espaço usando o novo ponto selecionado
    for i in range(X.shape[0]):
        
        for j in range(X.shape[1]):
            
            ponto_atual = (X[i, j], Y[i, j])
            Z[i, j] = 0
            
            for carga, pos_carga in valores_cargas:
                Z[i, j] += calcular_potencial(carga, pos_carga, ponto_atual)

    # Plotagem do gráfico de contorno (heatmap) atualizado
    cs = ax2.contourf(X, Y, Z, cmap='viridis')
    
    ax2.set_xlabel('Eixo x')
    ax2.set_ylabel('Eixo y')
    ax2.set_title('Gráfico de Contorno (Heatmap)')
    
    # fig.colorbar(cs, ax=ax2)

# ************************************************************************************************

def criar_linha_equipotencial(ax2, X, Y, Z, potencial_selecionado, nivel_potencial):        
    
    contour = ax2.contour(X, Y, Z, levels=[nivel_potencial], colors='g')
    ax2.clabel(contour, inline=True, fontsize=20, fmt={nivel_potencial: f'Equipotencial {nivel_potencial:.3f} V'})


def main():
    num_cargas = selecionar_quantidade_cargas()
    print(f"Quantidade de cargas selecionadas: {num_cargas}")

    valores_cargas = selecionar_valores_cargas(num_cargas)
    print("Valores das cargas selecionados:", valores_cargas)

    ax1, ax2 = desenhar_grafico_cargas(valores_cargas)

    X, Y, Z = criar_grafico_contorno(valores_cargas)
    atualizar_grafico_contorno(ax2, X, Y, Z, valores_cargas, (0, 0))

    while True:
        ponto_x, ponto_y = plt.ginput(1, timeout=-1)[0]
        ponto = (ponto_x, ponto_y)

        potencial_total = 0
        
        for carga, pos_carga in valores_cargas:
            
            potencial_total += calcular_potencial(carga, pos_carga, ponto)

        potencial_total = round(potencial_total, 3)

        print(f"Potencial elétrico no ponto ({ponto_x:.1f}, {ponto_y:.1f}): {potencial_total:.3f}")

        atualizar_grafico_contorno(ax2, X, Y, Z, valores_cargas, ponto)
        criar_linha_equipotencial(ax2, X, Y, Z, potencial_total, potencial_total)
        
        plt.draw()

if __name__ == "__main__":
    main()
