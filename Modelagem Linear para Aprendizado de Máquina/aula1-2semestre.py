# Preparando o ambiente:
from scipy.stats import norm

# Exercício 1)
# a)
print(norm.cdf(164, 175, 10))

# b)
print(norm.sf(164, 175, 10))

# ou

print(1 - norm.cdf(164, 175, 10))

#c)
a = norm.cdf(164, 175, 10)
b = norm.cdf(174, 175, 10)
print(b - a)