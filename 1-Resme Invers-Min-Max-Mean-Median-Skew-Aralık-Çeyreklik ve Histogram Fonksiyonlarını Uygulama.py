
# coding: utf-8

# In[31]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew


# In[32]:


def fonksiyon1(img):
    print("Resmin boyutu = ",img.ndim) 
    print("Resmin Shape değeri = ",img.shape)
    print("Kırmızı için min değer = ",img[:,:,0].min())
    print("Kırmızı için max değer = ",img[:,:,0].max()) # 0 kırmızı, 1 yeşil , 2 mavi
    print("Yeşil için min değer = ",img[:,:,1].min())
    print("Yeşil için max değer = ",img[:,:,1].max())
    print("Mavi için min değer = ",img[:,:,2].min())
    print("Mavi için max değer = ",img[:,:,2].max())


# In[33]:


def inverse1(x):
    return 255-x


# In[34]:


def inverse(image):
    image[:,:,0]=inverse1(image[:,:,0])
    image[:,:,1]=inverse1(image[:,:,1])
    image[:,:,2]=inverse1(image[:,:,2])


# In[35]:


def mean(image):
    print("Kirmizi ortalamasi : ",np.mean(image[:,:,0]))
    print("Yesil ortalamasi : ",np.mean(image[:,:,1]))
    print("Mavi ortalamasi : ",np.mean(image[:,:,2]))


# In[36]:


def median(image):
    print("Kirmizi median : ",np.median(image[:,:,0]))
    print("Yesil median : ",np.median(image[:,:,1]))
    print("Mavi median : ",np.median(image[:,:,2]))


# In[37]:


def mode(image):
    print("Kirmizi mode: ",stats.mode(image[:,:,0]))
    print("Yesil mode : ",stats.mode(image[:,:,1]))
    print("Mavi mode: ",stats.mode(image[:,:,2]))


# In[38]:


def my_H(image):
    H={}
    for i in range (image.shape[0]):
        for j in range (image.shape[1]):
            if(image[i,j,0] in H.keys()):
                H[image[i,j,0]]=H[image[i,j,0]]+1
            else:
                H[image[i,j,0]]=1
            if(image[i,j,1] in H.keys()):
                H[image[i,j,1]]=H[image[i,j,1]]+1
            else:
                H[image[i,j,1]]=1
            if(image[i,j,2] in H.keys()):
                H[image[i,j,2]]=H[image[i,j,2]]+1
            else:
                H[image[i,j,2]]=1
    plt.bar(list(H.keys()),list( H.values()), color='BLUE')
    plt.show()


# In[39]:


def ceyreklik(image):
    print("Kirmizi Q1 degeri = ",np.percentile(image[:,:,0],25))
    print("Kirmizi Q2 degeri = ",np.percentile(image[:,:,0],50))
    print("Kirmizi Q3 degeri = ",np.percentile(image[:,:,0],75))
    print("Yesil Q1 degeri = ",np.percentile(image[:,:,1],25))
    print("Yesil Q2 degeri = ",np.percentile(image[:,:,1],50))
    print("Yesil Q3 degeri = ",np.percentile(image[:,:,1],75))
    print("Mavi Q1 degeri = ",np.percentile(image[:,:,2],25))
    print("Mavi Q2 degeri = ",np.percentile(image[:,:,2],50))
    print("Mavi Q3 degeri = ",np.percentile(image[:,:,2],75))
    print("Kirmizi iqr degeri = ",iqr(image[:,:,0]))
    print("Yesil iqr degeri = ",iqr(image[:,:,1]))
    print("Mavi iqr degeri = ",iqr(image[:,:,2]))


# In[40]:


def skewness(image):
    print("Kirmizi skewness degeri = ",skew(image[:,:,0]))
    print("Yesil skewness degeri = ",skew(image[:,:,1]))
    print("Mavi skewness degeri = ",skew(image[:,:,2]))


# In[41]:


def aralik(image):
    print("Kirmizi range araligi = ",image[:,:,0].max()-image[:,:,0].min())
    print("Yesil range araligi = ",image[:,:,0].max()-image[:,:,1].min())
    print("Mavi range araligi = ",image[:,:,0].max()-image[:,:,2].min())


# In[62]:


img = plt.imread("turtle.jpg")
plt.imshow(img)
img.setflags(write=1) # resim sadece read-only özelliğine sahipti üzerinde değişiklik yapabilmek için değiştirdim
img.flags
inverse(img)
plt.imshow(img)


# In[66]:


fonksiyon1(img)
mean(img)
median(img)
ceyreklik(img)


# In[64]:


my_H(img)


# In[65]:


inverse(img)
plt.imshow(img)


# In[90]:


my_H(img)

