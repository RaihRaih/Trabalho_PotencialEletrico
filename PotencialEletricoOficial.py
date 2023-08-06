# Trabalho de Física - Potencial Elétrico
# Alberth Emanuel - Carolina Fonseca - Raissa Maia - Igor Amorim

#Extensões que serão usadas são: matplotlib, numpy e tkinter
import tkinter as tk
from tkinter import simpledialog

import matplotlib.pyplot as plt
import numpy as np


# ************************************************************************************************

# Função para selecionar a quantidade de cargas elétricas
def selecionar_quantidade_cargas():
    
     # Cria uma janela pop-up usando tkinter e pede ao usuário para selecionar a quantidade de cargas
    root = tk.Tk()
    root.withdraw()
    
    num_cargas = simpledialog.askinteger("Quantidade de Cargas", "Selecione a quantidade de cargas elétricas (1 a 4):", minvalue=1, maxvalue=4)
    root.destroy()
    
    return num_cargas

# ************************************************************************************************


#Função para selecionar os valores das cargas elétricas e suas posições
def selecionar_valores_cargas(num_cargas):
    
    # Cria uma janela pop-up usando tkinter e pede ao usuário para inserir os valores das cargas e suas posições
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

# ************************************************************************************************


# Função para calcular o potencial elétrico em um ponto causado por uma carga em uma posição
def calcular_potencial(carga, pos_carga, ponto):
    
    k = 9e9 # Constante eletrostática (k)
    
    # Cálculo da distância entre a carga e o ponto no espaço
    dx = ponto[0] - pos_carga[0]
    dy = ponto[1] - pos_carga[1]
    distancia = (dx*2 + dy2)*0.5
    
    return k * carga / distancia    # Cálculo do potencial elétrico usando a Lei de Coulomb

# ************************************************************************************************

# Função para criar o gráfico de contorno do potencial elétrico
def criar_grafico_contorno(cargas, resolucao = 100):
    
    # Definição das coordenadas do espaço em que o gráfico será criado
    x_min, x_max = -10, 10
    y_min, y_max = -10, 10
    
    x = np.linspace(x_min, x_max, resolucao)
    y = np.linspace(y_min, y_max, resolucao)
    
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)


# ************************************************************************************************

 # Cálculo do potencial elétrico em cada ponto do espaço e armazenamento nos valores de Z
    for i in range(resolucao):
        
        for j in range(resolucao):
            ponto = (X[i, j], Y[i, j])
            
            for carga, pos_carga in cargas:
                Z[i, j] += calcular_potencial(carga, pos_carga, ponto)

    return X, Y, Z

# ************************************************************************************************

## Criar gráfico das cargas.

def main():
    
    num_cargas = selecionar_quantidade_cargas()
    print(f"Quantidade de cargas selecionadas: {num_cargas}")
    
    valores_cargas = selecionar_valores_cargas(num_cargas)
    print("Valores das cargas selecionados:", valores_cargas)
    
    #Desenhar esse gráfico de contorno na tela juntamente com o gráfico das caragas.
    
if __name__ == "__main__":
    main()
