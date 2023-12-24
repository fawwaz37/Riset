import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

artist_name = "radit"
image_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'image')
image_path = os.path.join(image_folder, f'{artist_name}.png')
I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Kernel untuk operator gradien Sobel
Sx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Sy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# Deteksi tepi operator gradien Sobel
Jx = cv2.filter2D(I, cv2.CV_64F, Sx)
Jy = cv2.filter2D(I, cv2.CV_64F, Sy)
Jedge = np.sqrt(Jx**2 + Jy**2)

plt.imshow(Jedge, cmap='gray')
plt.title('Deteksi Tepi Gradien Sobel')
output_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
output_path = os.path.join(output_folder, f'{artist_name}_sobel.png')
plt.savefig(output_path)
