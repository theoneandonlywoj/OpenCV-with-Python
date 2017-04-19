
# coding: utf-8

# # OpenCV by Wojciech Orzechowski
# ### 19th April 2017 

# ### Loading and saving a picture in OpenCV

# In[1]:

import cv2

image = cv2.imread('./pictures/1/formula_student.jpg', cv2.IMREAD_COLOR) # By default it returns BGR
image2 = cv2.imread('./pictures/1/formula_student.jpg', cv2.IMREAD_GRAYSCALE)
print('The file has been successfully loaded (read).')
print("Shape of the color image:", image.shape) # 325 x 584 x 3 channels
print("Shape of the gray image:", image2.shape) # 325 x 584 x 1 channels

# In[2]:
cv2.imshow('Gray', image2)
# In[3]:
cv2.imwrite('./pictures/1/formula_student_gray.jpg', image2)
print('The file has been successfully saved (written).')
cv2.waitKey(0)
cv2.destroyAllWindows()

