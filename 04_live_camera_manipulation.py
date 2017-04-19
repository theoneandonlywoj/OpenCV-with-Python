
# coding: utf-8

# # OpenCV by Wojciech Orzechowski
# ### 19th April 2017 

# ### Live camera operations in OpenCV

# In[1]:

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))


# In[2]:

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


# In[3]:

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


# In[4]:

# When everything done, release the capture
cap.release()

