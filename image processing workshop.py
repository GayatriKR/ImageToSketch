#!/usr/bin/env python
# coding: utf-8

# In[56]:


import cv2


# In[57]:


img=cv2.imread('doreamon.png')


# In[58]:


img.shape


# In[59]:


img #bgr format


# In[60]:


import matplotlib.pyplot as plt #follows rgb format


# In[61]:


cv2.imshow("img",img)
cv2.waitKey(0)
# cv2.imshow("img",img)
cv2.destroyAllWindows()


# In[62]:


img.shape #3 is bgr


# In[63]:


img[0]


# In[64]:


rev_img= img[:,:,::-1] #reversing img to get rgb 


# In[65]:


def show_img(img_arr):
    rgb_arr=cv2.cvtColor(img_arr,cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_arr)
    plt.axis(False)


# In[66]:


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# In[67]:


show_img(gray_img)


# In[68]:


gray_img


# In[69]:


show_img(255-gray_img)
inverted_img=255-gray_img


# In[ ]:





# In[70]:


blur_img=cv2.GaussianBlur(inverted_img,(111,111),0)


# In[71]:


show_img(blur_img)


# In[72]:


sketch=cv2.divide(blur_img,inverted_img,scale=256.0)


# In[73]:


sketch


# In[74]:


show_img(sketch)


# In[ ]:




