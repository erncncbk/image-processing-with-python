# Written by Erencan Çabuk
# Given numpy array(img2.npy) convert to image  

import numpy as np 
from PIL import Image

ld1=np.load('img2.npy')          # Load numpy array(img2.npy)
ld1.size                         # Prints 899075
""" 
channel1 = ld[0]                 # ld[0]  --> Gives us channel number for array form
width1   = ld[1]                 # ld[1]  --> Gives us width number for array form
height1  = ld[2]                 # ld[2]  --> Gives us height number for array form
print((channel1,width1,height1))   # Prints --> (4 512 439)
"""
new_ld1=(ld1[3:])                                       # New array without first 3 numbers
reshaped_array1 = np.reshape(new_ld1,[439,512,4])       # Reshape new array  (439*512*4)=899072
change_type1    = reshaped_array1.astype(np.uint8)      # Change type(uint8= unsigned 8 bit image) for new array
shape_array1    = change_type1.shape                    # Shape for change array type
arr1=np.array(change_type1)                             # Make array format for change_type
img1 = Image.fromarray(arr1,mode='RGBA')                # Creates an image memory from an array
img1.size                                               # Prints (600,338)
img1.save("130403008HW01_1.png")                        # Save image
img1.show()                                             # Show image

