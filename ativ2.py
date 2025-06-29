import numpy as np
import matplotlib.pyplot as plt

altura, largura = 300, 300
imagem = np.ones((altura, largura, 3))  # Fundo branco

# Desenhar círculo vermelho
cx, cy, r = 150, 150, 60
for y in range(altura):
    for x in range(largura):
        if (x - cx)**2 + (y - cy)**2 <= r**2:
            imagem[y, x] = [1, 0, 0]  # vermelho

plt.imsave("cgpi2.png", imagem)
