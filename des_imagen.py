from skimage import io
import matplotlib.pyplot as plt
import numpy as np

file = 'img01.jpg'

image=io.imread(file)

image = image[:,:,1]

nn = image.shape
nx = nn[0]
ny = nn[1]

vec = np.reshape(image, nn[0]*nn[1])

#print((np.min(vec), np.max(vec)))

num_bins = 200

#plt.hist(vec, num_bins)

umbral = 80

imgB = image < umbral
img = image * imgB

i0 = 100
del1 = 2

j = 0
j0 = 0
while j < ny:
 if imgB[i0, j] == True:
  j0 = j
  break
 else:
  j = j+1

print(j0)

img[i0:i0+del1,:] = 100

plt.imshow(img)
plt.show()


'''
mat = np.ones((100,100))

del1 = 1
i0 = 50
j0 = 60

mat[i0-del1:i0+del1, j0-del1:j0+del1] = 0

plt.imshow(mat, cmap = "gray")
plt.show()
'''
