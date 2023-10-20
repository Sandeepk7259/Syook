#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bluetooth 


# In[ ]:





# In[ ]:


ble = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
ble.connect(("00:90:78:56:34:12", 1))


# In[ ]:


data = ble.recv(1024)


# In[ ]:


x_accel, y_accel, z_accel = np.frombuffer(data[14:20], dtype=np.uint16)


# In[ ]:


magnitude = np.sqrt(x_accel**2 + y_accel**2 + z_accel**2)


# In[ ]:


if magnitude > 0.1:
    print("The tag is moving")
else:
    print("The tag is stationary")


# In[ ]:





# In[ ]:





# In[ ]:




