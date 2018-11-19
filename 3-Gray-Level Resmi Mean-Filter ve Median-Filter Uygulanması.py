
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math


# In[12]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    return math.sqrt((a**2)*w1 + (b**2)*w2 + (c**2)*w3)


# In[13]:


def turn_rgb_to_gray_level(img):
    m,n=img.shape[0],img.shape[1]
    img_2 = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            img_2[i,j]=get_distance(img[i,j,:])
    return img_2


# In[14]:


def apply_mask_avg(p):
    return np.average(p)

def apply_mask_med(p):
    return np.median(p)


# In[15]:


img=plt.imread("turtle.jpg")
img_2=turn_rgb_to_gray_level(img)


# In[16]:


#mean filter
m,n=img_2.shape[0],img_2.shape[1]
img_3=np.zeros((m,n))
for i in range(m):
    for j in range(n):
        if(i==0 or j==0 or i==m or j==n):
            continue
        else:
            p=img_2[i-1:i+2,j-1:j+2]
            img_3[i,j]=apply_mask_avg(p)


# In[17]:


#median filter
img_4=np.zeros((m,n))
for i in range(m):
    for j in range(n):
        if(i==0 or j==0 or i==m or j==n):
            continue
        else:
            p=img_2[i-1:i+2,j-1:j+2]
            img_4[i,j]=apply_mask_med(p)


# In[25]:


plt.imshow(img)
plt.subplot(2,2,1),plt.imshow(img)
plt.subplot(2,2,2),plt.imshow(img_2,cmap='gray')
plt.subplot(2,2,3),plt.imshow(img_3,cmap='gray')
plt.subplot(2,2,4),plt.imshow(img_3,cmap='gray')

