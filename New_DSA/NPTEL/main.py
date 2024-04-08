import numpy as np

matrix = np.random.randint(1, 5, size=(4, 4))
print(matrix)
def blurring(matrix, blur_effect):
    for items in matrix:
        for i in range(blur_effect, len(items)-blur_effect):
            avg = np.mean(items[i-blur_effect:i+blur_effect])
            items[i] = avg

# blurring(matrix, 4)
# print(matrix)

import numpy as np

def blur_image(image, kernel_size=(3, 3)):
  
  # Handle odd kernel sizes for centering
  kernel_width, kernel_height = kernel_size
  pad_width = (kernel_width // 2, kernel_width // 2 + kernel_width % 2)
  pad_height = (kernel_height // 2, kernel_height // 2 + kernel_height % 2)
#   print(pad_width, pad_height)
  # Pad the image for border handling
  padded_image = np.pad(image, pad_width=(pad_height, pad_width), mode='edge')
  print(padded_image)
  # Initialize the blurred image
  blurred_image = np.zeros_like(image)

  # Iterate through each pixel of the original image
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      # Extract the image neighborhood based on kernel size
      neighborhood = padded_image[i:i+kernel_height, j:j+kernel_width]

      # Calculate the average intensity
      average_intensity = np.mean(neighborhood)

      # Assign the average intensity to the corresponding pixel in the blurred image
      blurred_image[i, j] = average_intensity

  return blurred_image

print(" ")

print(blur_image(matrix))
