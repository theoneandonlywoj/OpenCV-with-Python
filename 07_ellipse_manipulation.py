
# coding: utf-8

# # OpenCV by Wojciech Orzechowski
# ### 19th April 2017 

# ### Drawing in OpenCV

# In[1]:

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)


# # Ellipse

# - cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) 
# - Be aware that OpenCV counts angle clockwise, not counter-clockwise (observation).

# In[2]:

cv2.ellipse(img,(256,200),(50,50), -45, 90, 360 , 255, -1)


# In[3]:

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:



