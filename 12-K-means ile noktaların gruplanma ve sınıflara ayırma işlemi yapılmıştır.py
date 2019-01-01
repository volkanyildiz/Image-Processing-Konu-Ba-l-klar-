
# coding: utf-8

# In[62]:


# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

from mpl_toolkits import mplot3d
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

xdata=iris.data[:,0]
ydata=iris.data[:,2]
zdata=iris.data[:,3]
label=iris.target

ax.scatter3D(xdata[100:149], ydata[100:149], zdata[100:149],marker='o')
ax.scatter3D(xdata[50:99], ydata[50:99], zdata[50:99],marker='x')
ax.scatter3D(xdata[0:49], ydata[0:49], zdata[0:49],marker='x')


# In[2]:


X.shape


# In[7]:


iris.data.shape,iris.target.shape


# In[14]:


for i in range(0,3):
    print(iris.data[i],iris.target[i])
for i in range(50,53):
    print(iris.data[i],iris.target[i])
for i in range(100,103):
    print(iris.data[i],iris.target[i])


# In[48]:





# In[138]:


#5.1 3.5 1.4 0.2
def get_mu_s():
    mu_0=[5,2,0]
    mu_1=[4,4,0]
    mu_2=[3,2,5]
    
    return mu_0,mu_1,mu_2
def get_distance(mu,point):
    x=mu[0]-point[0]
    y=mu[1]-point[1]
    z=mu[2]-point[2]

    return (x**2+y**2+z**2)**0.5
def get_class_for_one_instance(flower):
    mu_s=get_mu_s()
    d_0=get_distance(mu_s[0],flower)
    d_1=get_distance(mu_s[1],flower)
    d_2=get_distance(mu_s[2],flower)
    if ((d_0 < d_1) and (d_0<d_2)):
        return "0"
    if ((d_1 < d_0) and (d_1<d_2)):
        return "1"
    if ((d_2 < d_1) and (d_2<d_0)):
        return "2"
def my_f_1(s_1=125):
    x=iris.data[s_1][0]
    y=iris.data[s_1][2]
    z=iris.data[s_1][3]
    my_f_1=[x,y,z]
    r=get_class_for_one_instance(my_f_1)
    print(r)
for i in range(150):
    my_f_1(i)


# In[122]:


def get_flower(i):
    x=iris.data[i][0]
    y=iris.data[i][2]
    z=iris.data[i][3]
    return [x,y,z]
     


# In[139]:


def update_mu():
    hata="yok"
    mu_0_counter=0.0001
    mu_0_sum=0
    
    mu_1_counter=0.0001
    mu_1_sum=0
    
    mu_2_counter=0.0001
    mu_2_sum=0
    
    c_1=[]
    c_2=[]
    c_3=[]
        
    for i in range(150):
        my_flower_data=get_flower(i)
        
        f_class=get_class_for_one_instance(my_flower_data)
        hata="var"

        #print(f_class)
        if(f_class=="0"):
            c_1.append(my_flower_data)    
        if(f_class=="1"):
            c_2.append(my_flower_data)
            
        if(f_class=="2"):
            c_2.append(my_flower_data)
            
    
    
    return c_1,c_2,c_3


# In[143]:


c_1,c_2,c_3=update_mu()


# In[144]:


len(c_1),len(c_2),len(c_3)

