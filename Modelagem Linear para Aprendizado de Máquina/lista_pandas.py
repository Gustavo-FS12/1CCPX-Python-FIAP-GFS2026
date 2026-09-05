# Preparo do ambiente:
import pandas as pd
import matplotlib.pyplot as plt

# Conjunto de Dados:
vendas_camisetas = pd.Series([2, 4, 3, 4, 5, 2, 4, 11, 4, 2])
print(vendas_camisetas)

# Análise Exploratória de Dados: Etapa de Estatística Descritiva
# Medidas de Tendência Central
# 1) Média: Esperança Matemática
print(vendas_camisetas.mean())

# 2) Mediana: Elemento central, separa o conjunto de dados ao meio, 50% dos dados ficam abaixo dela e 50% acima
print(vendas_camisetas.median())

# 3) Moda: Elemento com maior frequência absoluta
print(vendas_camisetas.mode())

# Medida de Disperção:
# 1) Máximo
print(vendas_camisetas.max())

# 2) Mínimo
print(vendas_camisetas.min())

# 3) Amplitude
print(vendas_camisetas.max() - vendas_camisetas.min())

# 4) Variância Amostral: Não é interpretável, pois a grandeza da variável é alterada
print(vendas_camisetas.var())

# 5) Desvio Padrão Amostral
print(vendas_camisetas.std())

# 6) Coeficiente de Variação Amostral:
print(vendas_camisetas.std() / vendas_camisetas.mean() * 100)

# Medidas Separativas
# Quartis
print(vendas_camisetas.quantile([0.25, 0.50, 0.75]))

# Análise Gráfica: Boxplot
plt.boxplot(vendas_camisetas,
            patch_artist=True,
            boxprops=dict(facecolor='red'))
plt.show()

print(vendas_camisetas.describe())

