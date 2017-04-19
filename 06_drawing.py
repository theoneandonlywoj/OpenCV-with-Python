
# coding: utf-8

# # OpenCV by Wojciech Orzechowski
# ### 19th April 2017 

# ### Drawing in OpenCV

# In[1]:

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)


# # Line

# In[2]:

# Draw a white line with thickness of 5 px
# cv2.line(image, (x_start, y_start), (x_end, y_end), (B,G,R), thickness)
# x and y must be integers
cv2.line(img,(0,0),(int(512/2), int(512/2)),(255,255,255), 5) 


# In[3]:

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Rectangle

# In[4]:

cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)


# In[5]:

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Circle

# In[6]:

cv2.circle(img,(35,63), 63, (0,0,255), -1)


# In[7]:

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Ellipse

# In[8]:

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


# In[9]:

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Polygon

# In[10]:

pts = np.array([[100,50],[100,100],[170,100],[100,50]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts], True ,(0,255,255))


# In[11]:

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Text

# In[12]:

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'by Arcyfelix',(10,500), font, 2,(255,255,255), 2 ,cv2.LINE_AA)


# In[13]:

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:



