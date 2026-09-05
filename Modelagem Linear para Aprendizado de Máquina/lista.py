
#Preparando o ambiente:
from collections import Counter
import matplotlib.pyplot as plt

'''
# Gráficos para Variáveis Qualitativas:
# Gráficos de Setores:
# 1) Conjunto de Dados:

dados1 = ["Sim"]*20 + ["Não"]*45
print(dados1)

resposta1 = Counter(dados1)
print(resposta1)

# 2) Construção Gráfica:
plt.pie(list(resposta1.values()),
        labels=list(resposta1.keys()),
        autopct='%1.2f%%',
        colors=['blue', 'red'])

plt.title('Resultado da Pesquisa Apliacada pelo McDonalds - 2026')
plt.legend(list(resposta1.keys()),
             loc='upper right')

plt.show()
'''

# Gráfico de Barras Verticais:
'''
dados1 = ["Sim"]*20 + ["Não"]*45
print(dados1)

resposta1 = Counter(dados1)
print(resposta1)

# 2) Construção Gráfica:
plt.bar(x=list(resposta1.keys()),
        height=list(resposta1.values()),
        color=['blue', 'red'])

plt.title('Resultado da Pesquisa Aplicada pelo Mcdonalds - 2026')
plt.legend(list(resposta1.keys()),
           loc='upper right')

plt.show()
'''

# Gráfico de Barras Horizontais: ERRO
'''
dados1 = ["Sim"]*20 + ["Não"]*45
print(dados1)

resposta1 = Counter(dados1)
print(resposta1)

# 2) Construção Gráfica:
plt.bar(x=list(resposta1.keys()),
        weidth=list(resposta1.values()),
        color=['blue', 'red'])

plt.title('Resultado da Pesquisa Aplicada pelo Mcdonalds - 2026')
plt.legend(list(resposta1.keys()),
           loc='upper right')

plt.show()
'''

# Gráficos para Variávies Quantitativas:
# 1) Conjunto de Dados:
'''
dados2 = [15, 17, 15, 15, 17, 14, 18, 15, 15, 17, 15, 12, 15, 16]
print(dados2)

plt.hist(dados2,
         bins=3,
         color='green')
plt.xlabel('Intervalo das Quantidades Vendidas de Camisetas')
plt.ylabel('Frequência Absoluta')
plt.title('Vendas da Startup FIAP STORE')
plt.show()
'''

# Gráfico Boxplot Vertical:
# 1) Conjunto de Dados:
'''
dados2 = [15, 17, 15, 15, 17, 14, 18, 15, 15, 17, 15, 12, 15, 16]
print(dados2)

plt.boxplot(dados,
            patch_artist=True,
            boxpross=dict(facecolor='green'))
plt.title('Vendas da Startup FIAP STORE')
plt.xlabel('Dados Coletados pela startup em 04/2026')
plt.ylabel('Quantidade de Camisetas Vendidas')
plt.show()
'''
# Gráfico Boxplot Horizontal:
# 1) Conjunto de Dados:
'''
dados2 = [15, 17, 15, 15, 17, 14, 18, 15, 15, 17, 15, 12, 15, 16]
print(dados2)

# 2) Construção Gráfica:
plt.boxplot(dados2,
            patch_artist=True,
            boxpross=dict(facecolor='green'))
plt.title('Vendas da Startup FIAP STORE')
plt.xlabel('Quantidade de Camisetas Vendidas')
plt.ylabel('Dados Coletados pela startup em 04/2026')
plt.show()
'''