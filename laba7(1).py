#Variant №16
#Y(x)=cos(x**2)/x

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,5)
y = np.cos(x**2)/x

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()

fig.savefig(input('Дайте назву графіку: '))
print("Ваш графік збереженний біля файла .py")
