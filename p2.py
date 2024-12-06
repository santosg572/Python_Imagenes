import matplotlib.pyplot as plt
import numpy as np

mat = np.ones((100,100))

del1 = 1
i0 = 50
j0 = 60

mat[i0-del1:i0+del1, j0-del1:j0+del1] = 0

plt.imshow(mat, cmap = "gray")
plt.show()

