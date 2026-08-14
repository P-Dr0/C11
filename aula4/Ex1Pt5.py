import numpy as np

np.random.seed(10)
mtz = np.random.randint(1, 51, (4, 4))
print(mtz)

media_linhas = mtz.mean(axis=1)
media_colunas = mtz.mean(axis=0)
print(media_linhas)
print(media_colunas)

print(media_linhas.max())
print(media_colunas.max())

valores, contagens = np.unique(mtz, return_counts=True)
for valor, contagem in zip(valores, contagens):
    print(f"{valor}: {contagem}")
