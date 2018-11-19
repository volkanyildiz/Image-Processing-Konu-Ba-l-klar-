
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import random as random


# In[11]:


#d) A şıkkında yazdığınız fonksiyonu kullanarak 100 farklı matris elde edip birinci 
#üretilen ile diğerlerini karşılaştırıp(distance) yakınlığını ve benzerliğini listeleyiniz
#100 tane A daki fonk çağır ordaki 100 tanesini 1. ile karşılaştır


# In[12]:


#28x28 boyutunda matris üretip içeriği rastgele 0 veya 1 ata
def my_create_m():
    return np.random.randint(0,2,(28,28))


# In[13]:


#28x28'lik matrisi parametre alan MBR dörgeni üreten fonksiyon
def MBR_create_28_by_28_with_0_1(matris_a):
    m=matris_a.shape[0]
    n=matris_a.shape[1]
    x_min=m
    x_max=0
    y_min=n
    y_max=0
    for i in range(m):
        for j in range(n):
            if(matris_a[i,j]==1):
                if (x_min>i):
                    x_min=i                          
                if (x_max<i):
                    x_max=i
                if (y_min>j):
                    y_min=j
                if (y_max<j):
                    y_max=j
    return (x_min,x_max,y_min,y_max)


# In[14]:


#Kendisine aktarılan iki vektörün benzerliğini return eden fonksiyon
def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity+character_a[i,j]*character_b[i,j]
    return my_similarity


# In[15]:


#28x28'lik matrisi 100 tane üretip benzerliklerin diziye yazan fonksiyon
def get_similarity_for_100_characters():
    dizi=[]
    for i in range(100):
        new_dizi=my_create_m()
        dizi.append(new_dizi)
    for i in range(100):
        benzerlik=get_similarity(dizi[0],dizi[i])
    return benzerlik


# In[17]:


a=my_create_m()
benzerlik_max=0
c=np.zeros((28,28))
for i in range(100):
    b=my_create_m()
    if(get_similarity(a,b)>benzerlik_max):
        benzerlik_max=get_similarity(a,b)
        c=b
        
print("En Yüksek Benzerlik : ",benzerlik_max)
plt.imshow(a,interpolation='nearest',cmap='gray')
plt.show()
plt.imshow(c,interpolation='nearest',cmap='gray')
plt.show()
    
print(get_similarity_for_100_characters())


# In[21]:


print(my_create_m())
print("MBR=",MBR_create_28_by_28_with_0_1(my_create_m()))
a_1=my_create_m()
a_2=my_create_m()
print("benzerlik=",get_similarity(a_1,a_2))

