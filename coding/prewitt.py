import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

artist_name = "radit"
image_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'image')
image_path = os.path.join(image_folder, f'{artist_name}.png')
I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Kernel untuk operator gradien Prewitt
Px = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
Py = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Deteksi tepi operator gradien Prewitt
Jx = cv2.filter2D(I, cv2.CV_64F, Px)
Jy = cv2.filter2D(I, cv2.CV_64F, Py)
Jedge = np.sqrt(Jx**2 + Jy**2)

plt.imshow(Jedge, cmap='gray')
plt.title('Deteksi Tepi Gradien Prewitt')
output_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
output_path = os.path.join(output_folder, f'{artist_name}_prewitt.png')
plt.savefig(output_path)
