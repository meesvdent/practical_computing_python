from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_gradient_magnitude
import matplotlib.pyplot as plt

# load image and convert to matrix using asarray
img = np.asarray(Image.open('./100809wt-t090-p08.tif'))
# What is the nature of the data/ size of the image
print(img.dtype, img.shape)  #Prints "uint8 (512, 712)"
#calculate gradient magnitude; but first cast to float32 image
mag = gaussian_gradient_magnitude(img.astype(np.float32), 4)  # originally 4
#normalize; then cast back to 8 bit unsigned int
mag *= 255.0 / np.max(mag)
mag=mag.astype(np.uint8)
#choose a colormap
cm = plt.cm.magma
# Apply the colormap like a function:
colored_image = cm(mag)
print("range colored_image: ", np.min(colored_image), ", ", np.max(colored_image))
inverted_image = 1 - colored_image
print(colored_image.dtype,colored_image.shape)  #float64 (512, 712, 4)
# This is a 4-channel image (R,G,B,A) in float [0, 1]
# Convert to RGB in uint8 and save it:
result = Image.fromarray((colored_image[:, :, :3] * 255).astype(np.uint8))
inverted_result = Image.fromarray((inverted_image[:, :, :3] * 255).astype(np.uint8))
result.save('nuclei_gradient_CM2.png', format="PNG")
inverted_result.save('inverted_nuclei_gradient_CM2.png', format="PNG")


