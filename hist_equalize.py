# Created on Thu Nov  8 15:06:30 2018

# @author: Erencan CABUK

import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image 
import sys
#%%
ld=np.load(sys.argv[1])          
ld.size                         
c = ld[0]                 
w = ld[1]                
h = ld[2]     
pixel = h*w            
#%%
new_ld=(ld[3:])                                       
reshaped_array = np.reshape(new_ld,[h,w])        
change_type    = reshaped_array.astype(np.uint8)      
shape_array    = change_type.shape                    
arr=np.array(change_type)                             
img = Image.fromarray(arr,mode='L')  
img.show()
hist = img.histogram()
hist = np.array(hist)
p    = np.true_divide(hist, np.sum(hist))
cdf  = hist.cumsum()
cdf  = (255 * cdf /cdf[-1])   # Normalize
#%%
T = np.around(cdf)
img_eq =Image.eval(img,lambda x: T[x])
img_eq.show()
hist_eq  = img_eq.histogram()
psk = np.true_divide(hist_eq,np.sum(hist_eq))
#%%
plt.figure(figsize = (10,20))
plt.subplots_adjust ( hspace=0.50)
fsize=20
plt.subplot(3,1,1)
plt.stem (p)
plt.xlim((0,255))
plt.ylim((0,np.max(p)))
plt.xlabel('$r_k$',fontsize=fsize)
plt.ylabel('$p(r_k)$',fontsize= fsize)
plt.title ('pdf of intensity values in the source image')
#%%
plt.subplot(3,1,2)
plt.stem(psk)
plt.xlim((1,256))
plt.ylim((0,np.max(psk)))
plt.xlabel('$s_k$',fontsize=fsize)
plt.ylabel('$p_e(s_k)$',fontsize= fsize)
plt.title ('pdf of intensity values in the equalized image')
#%%
plt.subplot(3,1,3)
plt.step(range(0,256,1),cdf)
plt.xlim((0,255))
plt.ylim(0,256)
plt.xlabel('$r_k$',fontsize=fsize)
plt.ylabel('$s_k$',fontsize= fsize)
plt.title ('Corresponding Transformation function $T(r_k)$ ')
plt.savefig('130403008HW02.png')
