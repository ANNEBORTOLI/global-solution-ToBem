'''TôBem - Matemática (Differentiated Problem Solving)
Integrantes: Gabriel Almeida (RM: 575525) e Anne Bortoli (RM: 574750)
Preparando o ambiente: pip install numpy matplotlib'''
 
import numpy as np                # numpy: cria listas de números e faz contas com elas
import matplotlib.pyplot as plt   # matplotlib: desenha os gráficos
 
# ---------- Modelo 1: temperatura do dia (função de 2º grau) ----------
# T(x) = -0,08*(x - 15)**2 + 34, onde x é a hora do dia
# Pico de 34 °C às 15 h (o "15" e o "34" da fórmula); o -0,08 deixa a curva larga, como um dia real
 
x = np.linspace(6, 24, 100)           # 100 horas igualmente espaçadas, de 6 h até 24 h
y = -0.08 * (x - 15) ** 2 + 34        # calcula a temperatura T de cada hora x de uma vez só
 
plt.plot(x, y, label="Função de 2 Grau T(x) = -0,08(x-15)**2 + 34", color="blue")  
plt.axhline(28, label="28 °C: atenção", color="orange")   
plt.axhline(32, label="32 °C: perigo", color="red")       
plt.title("Temperatura do apartamento ao longo do dia")  
plt.xlabel("Domínio da Função: Hora do dia")              
plt.ylabel("Imagem da Função: Temperatura (°C)")          
plt.legend()                                              
plt.grid()                                               
plt.show()                                                
 
# Quando a temperatura chega a 32 °C?
a = -0.08                             # número que multiplica x²
b = 2.4                               # número que multiplica x
c = -16                               # número sozinho (16 - 32)
delta = b**2 - 4*a*c                  # Bhaskara: delta = 5,76 - 5,12 = 0,64
x1 = (-b + np.sqrt(delta)) / (2*a)    # primeira raiz (hora em que passa de 32 °C)
x2 = (-b - np.sqrt(delta)) / (2*a)    # segunda raiz (hora em que volta abaixo de 32 °C)
print("A temperatura chega a 32 °C às", round(x1, 1), "h e às", round(x2, 1), "h")  # 10 h e 20 h
print("Horas em perigo de calor:", round(x2 - x1, 1))   # diferença entre as duas horas = 10 h
 
# ---------- Modelo 2: preocupação sem check-in (função de 1º grau) ----------
# R(x) = x/13, onde x é o tempo (em horas) desde o último check-in
# 13 é o prazo de PERIGO do sensor: em 13 h a preocupação chega a 1 (o máximo)
 
x = np.linspace(0, 13, 100)           # de 0 h até 13 h sem check-in
y = x / 13                            # preocupação de cada tempo x (vai de 0 até 1)
 
plt.plot(x, y, label="Função de 1 Grau R(x) = x/13", color="purple")   
plt.axvline(12, label="12 h: atenção", color="orange")    
plt.axvline(13, label="13 h: perigo", color="red")        
plt.title("Preocupação sem check-in")                    
plt.xlabel("Domínio da Função: Horas desde o último check-in") 
plt.ylabel("Imagem da Função: Preocupação (0 a 1)")            
plt.legend()                                              
plt.grid()                                                
plt.show()                                                
 
print("Preocupação com 12 h sem check-in:", round(12 / 13, 2))  # 12/13 = 0,92
 
# ---------- Indicador de impacto ----------
atual = 24   # horas até alguém verificar hoje (caso real, da Ficha)
meta = 1     # meta do protótipo: verificar em até 1 hora
print("Redução do tempo até a verificação:", round((atual - meta) / atual * 100, 1), "%")  # (24-1)/24 = 95,8 %
 