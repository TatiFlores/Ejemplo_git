'''
Este codigo sirve para blablabla
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,15)
plt.plot(x, np.sin(x), 'o')
plt.show()
plt.savefig("Seno.png")
