# Written by Erencan Çabuk
# Given numpy array(img1.npy) convert to image  

import numpy as np 
from PIL import Image

ld=np.load('img1.npy')          # Load numpy array(img1.npy)
ld.size                         # Prints 202803
""" 
channel = ld[0]                 # ld[0]  --> Gives us channel number for array form
width   = ld[1]                 # ld[1]  --> Gives us width number for array form
height  = ld[2]                 # ld[2]  --> Gives us height number for array form
print((channel,width,height))   # Prints --> (1 600 338)
"""
new_ld=(ld[3:])                                       # New array without first 3 numbers
reshaped_array = np.reshape(new_ld,[338,600])         # Reshape new array  (338*600*1)=202800
change_type    = reshaped_array.astype(np.uint8)      # Change type(uint8= unsigned 8 bit image) for new array
shape_array    = change_type.shape                    # Shape for change array type
arr=np.array(change_type)                             # Make array format for change_type
img = Image.fromarray(arr,mode='L')                   # Creates an image memory from an array
img.size                                              # Prints (600,338)
img.save("130403008HW01.png")                         # Save image
img.show()                                            # Show image

