import numpy as np
import cv2

def bit_plane_slicing(image):
    # Initialize an empty list to store the bit planes
    bit_planes = []

    # Iterate through each bit position (from 0 to 7)
    for bit_position in range(8):
        # Create a mask for the current bit plane (bitwise AND operation)
        mask = 1 << bit_position
        # Extract the current bit plane by applying the mask
        bit_plane = np.bitwise_and(image, mask)

        # Normalize the pixel values to the range [0, 255]
        bit_plane = bit_plane * 4

        # Append the bit plane to the list
        bit_planes.append(bit_plane)

    return bit_planes

image = np.random.randint(0, 4, size=(4, 4), dtype=(np.uint8))
sliced = bit_plane_slicing(image)
print(image)
print('\n')
print(sliced[7])

# cv2.imshow('Original image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
