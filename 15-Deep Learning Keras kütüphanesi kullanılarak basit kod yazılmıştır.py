
# coding: utf-8

# In[ ]:


from keras.datesets import mnist(train_images,train_labels),(test_images,test_labels)=mnist.load.data()
from keras import models
from keras import layers


# In[ ]:


network=models.sequential()


# In[ ]:


network.add(layers.Dense(512,activition='sigmaid',input.shape(28*28)))


# In[ ]:


network.add(layers.Dense(10,activition='sottmax'))


# In[ ]:


network.compile(optimizer='rmsprop',loss='categorized_entropy',matrics=[accuracy])


# In[ ]:


network.fit(train_images,train_labels,epoch=5,batch_size=128)

