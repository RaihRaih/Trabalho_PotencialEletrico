# Trabalho de Física - Potencial Elétrico
# Alberth Emanuel - Carolina Fonseca - Raissa Maia - Igor Amorim

#Extensões que serão usadas são: matplotlib, numpy e tkinter
import tkinter as tk
from tkinter import simpledialog

import matplotlib.pyplot as plt
import numpy as np

# Função para selecionar a quantidade de cargas elétricas
def selecionar_quantidade_cargas():
    
     # Cria uma janela pop-up usando tkinter e pede ao usuário para selecionar a quantidade de cargas
    root = tk.Tk()
    root.withdraw()
    
    num_cargas = simpledialog.askinteger("Quantidade de Cargas", "Selecione a quantidade de cargas elétricas (1 a 4):", minvalue=1, maxvalue=4)
    root.destroy()
    
    return num_cargas


def main():
    
    num_cargas = selecionar_quantidade_cargas()
    print(f"Quantidade de cargas selecionadas: {num_cargas}")
    
    
if __name__ == "__main__":
    main()

# Função para calcular o potencial elétrico em um ponto causado por uma carga em uma posição

# Função para criar o gráfico de contorno do potencial elétrico

# Definição das coordenadas do espaço em que o gráfico será criado
