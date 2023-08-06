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





def main():
    
    num_cargas = selecionar_quantidade_cargas()
    print(f"Quantidade de cargas selecionadas: {num_cargas}")
    
    valores_cargas = selecionar_valores_cargas(num_cargas)
    print("Valores das cargas selecionados:", valores_cargas)
    
    
if __name__ == "__main__":
    main()