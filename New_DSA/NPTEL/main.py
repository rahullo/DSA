import numpy as np

matrix = np.random.randint(1, 5, size=(4, 4))
# print(matrix)
def blurring(matrix, blur_effect):
    for items in matrix:
        for i in range(blur_effect, len(items)-blur_effect):
            avg = np.mean(items[i-blur_effect:i+blur_effect])
            items[i] = avg

# blurring(matrix, 4)
# print(matrix)

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

# print(" ")

# print(blur_image(matrix))

# print(matrix)

def delete_every_other_row_and_column(arr, scale):
    # Get the number of rows and columns in the array
    num_rows, num_cols = len(arr), len(arr[0])
    
    # Create a new 2D array to store the result
    result = []
    
    # Iterate through the rows of the array
    for i in range(0, num_rows, scale):
        row = []
        # Iterate through the columns of the array
        for j in range(0, num_cols, scale):
            # Append the value at the current row and column to the new array
            row.append(arr[i][j])
        # Append the row to the result array
        result.append(row)
    
    return result

def duplicate_rows_and_columns(arr):
  # Get the dimensions of the input array
  rows, cols = len(arr), len(arr[0])
  
  # Create a new 2D array to store the result
  result = [[0] * (2 * cols) for _ in range(2 * rows)]
  
  # Iterate over the rows of the input array
  for i in range(rows):
      # Iterate over the columns of the input array
      for j in range(cols):
          # Duplicate the current element in the result array
          result[2*i][2*j] = arr[i][j]
          result[2*i][2*j+1] = arr[i][j]
          result[2*i+1][2*j] = arr[i][j]
          result[2*i+1][2*j+1] = arr[i][j]
  
  return result

# Example usage:
input_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# result_array = duplicate_rows_and_columns(input_array)
# for row in result_array:
#     print(row)


# Example usage:
# Create a sample 2D array

# result = delete_every_other_row_and_column(matrix, 2)

# print(result)


arr1 = np.random.randint(0, 2, size=(5, 5), dtype=np.uint8)
arr2 = np.random.randint(0, 2, size=(5, 5), dtype=np.uint8)
print(arr1)
print(arr2)
print("\n")
def logic_Operation(arr1, arr2):
  ans = []
  for i in range(len(arr1)):
    row = []
    for j in range(len(arr1[0])):
        row.append(arr1[i][j] and arr2[i][j])
    ans.append(row)
  return ans
print(np.array(logic_Operation(arr1, arr2)))