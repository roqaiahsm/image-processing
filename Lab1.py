import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
img = cv2.imread('cameraman.jpg')
plt.imshow(img)
plt.show()
img2 = Image.open('cameraman.jpg')
plt.imshow(img2, cmap=cm.Greys_r)
plt.show()
# Task 3: Image Storing
cv2.imwrite('new_image.jpg', img)

img2.convert('RGB').save('new_image2.jpg')


# Task 4: Display Image as an Array
print(img.shape)
print(img)

img_array = np.array(img2)

print(img_array.shape)
print(img_array)
# Assessment: NumPy operations
print(img_array.ndim)
print(np.mean(img_array))
print(np.min(img_array))
print(np.max(img_array))
