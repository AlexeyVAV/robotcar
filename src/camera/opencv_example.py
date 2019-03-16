import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('images/motorway1.jpg',1)

laplacian = cv2.Laplacian(img, ddepth=cv2.CV_32F, ksize=17, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

images = [img,laplacian]
titles = ['original', 'laplacian']

for i in range(len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i]),
    plt.xticks([]),plt.yticks([])

plt.show()
# show images
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27 :
#     cv2.destroyAllWindows()

