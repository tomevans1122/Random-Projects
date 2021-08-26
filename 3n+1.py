# The Collatz

import matplotlib.pyplot as plt
import numpy as np

def collatz(i):
    lst = []
    if i == 1:
        lst = [4.0, 2.0]
    else:
        while i != 1:
            if i % 2 == 0:
                i = i / 2
                lst.append(i)
                continue
            else:
                i = i * 3 + 1
                lst.append(i)
                continue
    return lst


for i in range(1,21):
    x = collatz(i)
    arrayed_y = np.array(x)
    arrayed_x = np.arange(1, len(x) + 1)
    plt.plot(arrayed_x, arrayed_y, label= i)
plt.legend()
plt.xlabel("Chosen integers")
plt.ylabel("Values attained for integers subject to the Collatz loop")
plt.title("A representation of integers 1 to 20 subject to the Collatz Conjecture")
plt.show()


