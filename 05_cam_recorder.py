
# coding: utf-8

# # OpenCV by Wojciech Orzechowski
# ### 19th April 2017 

# ### Live camera recorded in OpenCV

# In[1]:

import numpy as np
import cv2

cap = cv2.VideoCapture(0)


# In[2]:

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./videos/3/output.avi', fourcc, 60.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame_flipped = cv2.flip(frame,0)
        # write the frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

