
# coding: utf-8

# # OpenCV by Wojciech Orzechowski
# ### 11th April 2017

# ### Loading OpenCV

# In[22]:

import cv2
import numpy as np
import os


# In[25]:

# Creating an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)
# It can be done by numpy.random.randint(0, 256, 120000) as well

# ### Creating and saving a random gray image

# In[26]:

grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('./pictures/RandomGray.png', grayImage)


# ### Creating and saving a random BGR image

# In[27]:

bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('./pictures/RandomColor.png', bgrImage)

