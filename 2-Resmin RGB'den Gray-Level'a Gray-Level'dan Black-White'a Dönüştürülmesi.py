
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# In[6]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c= v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w[0] + (b**2)*w[1] +(c**2)*w[2])**.5
    return d


# In[7]:


def convert_rgb_to_gray_level(img):
    m=img.shape[0]
    n=img.shape[1]
    img_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            img_2[i,j]=get_distance(img[i,j,:])
    return img_2


# In[8]:


def convert_gray_level_to_BW(img):
    m=img.shape[0]
    n=img.shape[1]
    img_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if img[i,j] > 120:
                img_bw[i,j]=1
            else:
                img_bw[i,j]=0
    return img_bw


# In[12]:


img =mpimg.imread("turtle.jpg")
get_ipython().run_line_magic('matplotlib', 'inline')

im_2=convert_rgb_to_gray_level(img)
im_3=convert_gray_level_to_BW(im_2)

plt.imshow(img)
plt.subplot(1,3,1),plt.imshow(img)
plt.subplot(1,3,2),plt.imshow(im_2,cmap='gray')
plt.subplot(1,3,3),plt.imshow(im_3,cmap='gray')

