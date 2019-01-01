
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# In[25]:


def my_product_two_dim_with_treshold(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]


# In[19]:


def get_my_data():
    my_data_x=[]
    my_data_x.append([1,0,0])
    my_data_x.append([1,0,1])
    my_data_x.append([1,1,0])
    my_data_x.append([1,1,1])
    my_data_x
    
    my_data_y=[]
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(1)
    my_data_y
    return my_data_x,my_data_y


# In[20]:


x,y=get_my_data()
for a,b in zip(my_data_x,my_data_y):
    print(a,b)


# In[21]:


def get_parameters():
    w=[]
    w.append(300)
    w.append(200)         #random y
    w.append(100)
    w
    learning_rate=1     #random y
    epoch=100
    
    return w,learning_rate,epoch
get_parameters()


# In[36]:


w,learning_rate,epoch=get_parameters()
samples,output=get_my_data()
samples


# In[38]:


output


# In[51]:


for i in range(epoch):
    error="hata_yok"
    s=-1
    i=0
    for each_sample,d in zip(samples,output):
        s=s+1
        i=i+1
        print("agirlik = ",w)
        print("ornek = ",each_sample)
        print("gercek_output",d)
        u=my_product_two_dim_with_treshold(each_sample,w)
        if(u>0):
            y=1
        else:
            y=0
        print("tahmin cikti =",y)
        print("")
        
        if(y!=d):   #error var
            for s in range(3):
                w[s]=w[s]-learning_rate*(y-d)*each_sample[s]
            error="hata_var"
    if(error == "hata_yok"):
        print("hata yok",i)
        break
    print(w)

