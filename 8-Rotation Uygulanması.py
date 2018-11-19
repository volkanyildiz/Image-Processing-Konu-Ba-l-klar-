
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.misc import imrotate


# In[14]:


img =mpimg.imread("turtle.jpg")

plt.imshow(img)
plt.show()


# In[23]:


img_2 = imrotate(img, 180)

plt.imshow(img_2)
plt.show()

