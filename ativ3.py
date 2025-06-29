import numpy as np
import matplotlib.pyplot as plt

altura, largura = 300, 300
imagem = np.ones((altura, largura, 3))  # Fundo branco

# Círculo azul
cx, cy, r = 80, 80, 40
for y in range(altura):
    for x in range(largura):
        if (x - cx)**2 + (y - cy)**2 <= r**2:
            imagem[y, x] = [0, 0, 1]

# Triângulo verde (usa fórmula de barycentric coordinates – simples)
def dentro_triangulo(px, py):
    ax, ay = 180, 50
    bx, by = 230, 130
    cx_, cy_ = 130, 130
    area = abs((bx - ax)*(cy_ - ay) - (cx_ - ax)*(by - ay))
    area1 = abs((ax - px)*(by - py) - (bx - px)*(ay - py))
    area2 = abs((bx - px)*(cy_ - py) - (cx_ - px)*(by - py))
    area3 = abs((cx_ - px)*(ay - py) - (ax - px)*(cy_ - py))
    return area == area1 + area2 + area3

for y in range(altura):
    for x in range(largura):
        if dentro_triangulo(x, y):
            imagem[y, x] = [0, 1, 0]

# Quadrado vermelho
for y in range(180, 240):
    for x in range(100, 160):
        imagem[y, x] = [1, 0, 0]

plt.imsave("cgpi3.png", imagem)
