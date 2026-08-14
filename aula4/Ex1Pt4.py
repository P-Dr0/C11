import numpy as np

mtz = np.random.randint(1, 10, (3, 5))
print(mtz)

total_elementos = mtz.size

if total_elementos % 2 == 0:
    print("A matriz poderia virar um vetor com número PAR de elementos")
else:
    print("A matriz poderia virar um vetor com número ÍMPAR de elementos")