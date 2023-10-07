from helper_functions import *
total=0


datafolder = "A:/assign/assgn1code/images/" #image destination folder 
imgpath = datafolder + "1.jpg" 
# Converting the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2

# Creating a data structure to store updated pixel information
temp = [0] * numb_colns
new_pixel_values = [temp[:] for _ in range(numb_rows)]
# A 3 x 3 mask as a tuple of tuples
mask = ((-1,-1,-1),(-1,8,-1),(-1,-1,-1))

# Implementing a function to slice a part from the image as a 2D list
def get_slice_2d_list(pixel_values, i, j):
    return [row[j-1:j+2] for row in pixel_values[i-1:i+2]]


# Implementing a function to flatten a 2D list or a 2D tuple
def flatten(two_d_list):
    return [item for sublist in two_d_list for item in sublist]

# For each of the pixel values, excluding the boundary values
for i in range(1, numb_rows + 1):
    for j in range(1, numb_colns + 1):
        # Creating little local 3x3 box using list slicing
        neighbour_pixels = get_slice_2d_list(pixel_values, i, j)
        # Applying the mask
        mult_result = [x * y for x, y in zip(flatten(neighbour_pixels), flatten(mask))]
        # adding all the multiplied values and set the new pixel value
        new_pixel_values[i - 1][j - 1] = sum(mult_result)      
for i in range(1, numb_rows+1):
    for j in range(1, numb_colns+1):
        print(new_pixel_values[i-1][j-1], end=" ")
        total=total+new_pixel_values[i-1][j-1]
        
    print("\n\n\n")


print("pixel value is ",total) 
# Verifying the  result
verify_result(pixel_values, new_pixel_values, mask)
# Displaying the original image and the edges of the image
view_images(imgpath, new_pixel_values)