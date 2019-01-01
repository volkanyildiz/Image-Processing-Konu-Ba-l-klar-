
# coding: utf-8

# In[8]:


import math
import matplotlib.pyplot as plt
import numpy as np


# In[9]:


myPoint_1=[0,0]
myPoint_2=[1,0]
myPoint_3=[0,1]
myPoint_4=[1,1]


# In[10]:


def myDistance(a,b):
    myPoint_1=a
    myPoint_2=b
    a=(myPoint_1[0]-myPoint_2[0])**2
    b=(myPoint_1[1]-myPoint_2[1])**2
    return math.sqrt(a+b)
myDistance(myPoint_2,myPoint_3)


# In[11]:


a=myPoint_1[0]+myPoint_2[0]+myPoint_3[0]+myPoint_4[0]
b=myPoint_1[1]+myPoint_2[1]+myPoint_3[1]+myPoint_4[1]
center_Point=(a/4,b/4)
center_Point


# In[12]:


def findCenter (List_Of_Points):
    a=0
    b=0
    for point in List_Of_Points:
        a=a+point[0]
        b=b+point[1]
    l=len(List_Of_Points)
    return (a/l,b/l)


# In[13]:


my_Point_List=[]
my_Point_List.append(myPoint_1)
my_Point_List.append(myPoint_2)
my_Point_List.append(myPoint_3)
my_Point_List.append(myPoint_4)
center=findCenter(my_Point_List)
center


# In[14]:


my_Array=np.array([[1,2,3],[2,6,9]],np.int32)
my_Array.ndim,my_Array.shape
my_Array_1=my_Array.reshape(1,6)
print(my_Array)
print("")
print(my_Array_1)


# In[15]:


array=["a1.jpg","a2.jpg","a3.jpg","a4.jpg","a5.jpg","b1.jpg","b2.jpg","b3.jpg","b4.jpg","b5.jpg","c1.jpg","c2.jpg","c3.jpg","c4.jpg","c5.jpg","d1.jpg","d2.jpg","d3.jpg","d4.jpg","d5.jpg","e1.jpg","e2.jpg","e3.jpg","e4.jpg","e5.jpg"]
array2=[]
for k in range(25):
    img1 = plt.imread(array[k])
    img1.ndim
    img1.shape
    img3 = np.zeros(img1.shape[0:2])
    img3.shape
    threshold = 128
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            n = img1[i,j,0]/3 + img1[i,j,1]/3 + img1[i,j,2]/3
            #img3[i,j] = n
            if n > threshold:
                img3[i,j] = 255
            else:
                img3[i,j] = 0

    plt.imshow(img3, plt.cm.gray)
    plt.show()
    img3=np.array(img3,np.int32).reshape(1,10000)
    array2.append(img3)


# In[18]:


Center_a=np.zeros((1,10000))
Center_b=np.zeros((1,10000))
Center_c=np.zeros((1,10000))
Center_d=np.zeros((1,10000))
Center_e=np.zeros((1,10000))

for i in range(0,25):
    if i<5:
        Center_a=Center_a+array2[i]
        
    elif i<10:
        Center_b=Center_b+array2[i]
        
    elif i<15:
        Center_c=Center_c+array2[i]
        
    elif i<20:
        Center_d=Center_d+array2[i]
        
    else:
        Center_e=Center_e+array2[i]
        


# In[19]:


Center_a=Center_a/5
Center_b=Center_b/5
Center_c=Center_c/5
Center_d=Center_d/5
Center_e=Center_e/5
print(Center_a)
print(Center_b) 
print(Center_c) 
print(Center_d) 
print(Center_e)

test=plt.imread("test.jpg")
test.ndim
test.shape
threshold=128

test1= np.zeros(test.shape[0:2])
test1.shape
for i in range(test.shape[0]):
        for j in range(test.shape[1]):
            n = test[i,j,0]/3 + test[i,j,1]/3 + test[i,j,2]/3
            if n > threshold:
                test1[i,j] = 255
            else:
                test1[i,j] = 0
test1=np.array(test1,np.int32).reshape(1,10000)

distA = np.linalg.norm(Center_a-test1)
distB = np.linalg.norm(Center_b-test1)
distC = np.linalg.norm(Center_c-test1)
distD = np.linalg.norm(Center_d-test1)
distE = np.linalg.norm(Center_e-test1)


# In[20]:


array3=[]
array3.append(distA)
array3.append(distB)
array3.append(distC)
array3.append(distD)
array3.append(distE)
print(array3)

array3.sort()
print(array3)
    
if (array3[0]==distA):
    print("Yazdığınız Karakter a")
elif (array3[0]==distB):
    print("Yazdığınız Karakter b")
elif (array3[0]==distC):
    print("Yazdığınız Karakter c")
elif (array3[0]==distD):
    print("Yazdığınız Karakter d")
elif (array[0]==distE):
    print("Yazdığınız Karakter e")
    

