import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

i1 = 0
i2 = 591
j1 = 0
j2 = 394

mat = np.zeros((i2, j2))
print(mat.shape)
mat[i1+1,] = 1
mat[i2-2,] = 1

mat[:,j1+1] = 1
mat[:,j2-1] = 1

x = np.arange(j2)
print(x)
y = np.round(10*np.cos(x)+12)
print(y)


for j in x:
 print((j, y[j]))
 mat[int(y[j]),int(j)] = 1

#img = mpimg.imread('image.jpg') # Load the image
plt.imsave('mati.jpg', mat) # Save the image

