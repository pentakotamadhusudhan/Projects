#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pytesseract
from PIL import Image

# In[11]:


pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

# In[25]:


file_path = 'image.png'
file_path = '3.png'


# In[13]:


def img_to_text(file_path):
    myconfig = r"--psm 11 oem 3"  # ocr engine mode
    text = pytesseract.image_to_string(Image.open(file_path), config=myconfig)
    return text


# In[27]:

myconfig = r"--psm 11 oem 3"  # ocr engine mode
text = pytesseract.image_to_string(Image.open(file_path), config=myconfig)

# In[28]:


print(text)

# In[30]:


text.splitlines()

# In[31]:


with open('test_output.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# In[ ]:


# In[17]:


with open('test_output.txt', 'r') as f:
    d = f.read()

# In[18]:


d

# In[19]:


from pdf2image import convert_from_path

# In[20]:


images = convert_from_path('list.pdf')

# In[21]:


len(images)

# In[23]:


images[2].save('3.png')

# In[1]:


import cv2

# In[2]:


img = cv2.imread('3.png')

# In[3]:


print(img.shape)

# In[4]:


cv2.imshow('show', img)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

# In[5]:


cv2.imwrite('c3.png', img[107:2108, 66:1577])

# In[16]:


img = cv2.imread('c3.png')
print(img.shape)

# In[17]:


# https://learnopencv.com/cropping-an-image-using-opencv/

image_copy = img.copy()
imgheight = img.shape[0]
imgwidth = img.shape[1]

# M = 76
# N = 104

# M = 200
# N = 504
M = 200
N = 500

x1 = 0
y1 = 0

for y in range(0, imgheight, M):
    for x in range(0, imgwidth, N):
        if (imgheight - y) < M or (imgwidth - x) < N:
            break

        y1 = y + M
        x1 = x + N

        # check whether the patch width or height exceeds the image width or height
        if x1 >= imgwidth and y1 >= imgheight:
            x1 = imgwidth - 1
            y1 = imgheight - 1
            # Crop into patches of size MxN
            tiles = image_copy[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= imgheight:  # when patch height exceeds the image height
            y1 = imgheight - 1
            # Crop into patches of size MxN
            tiles = image_copy[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= imgwidth:  # when patch width exceeds the image width
            x1 = imgwidth - 1
            # Crop into patches of size MxN
            tiles = image_copy[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            # Crop into patches of size MxN
            tiles = image_copy[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)

# In[35]:


import os

names = []
fh = []
for file in os.listdir('patches'):
    file_path = os.path.join('patches', file)
    if not file_path.endswith('.jpg'):
        continue
    text = img_to_text(file_path)
    data = (text.splitlines())
    print(data, len(data))
    print("=" * 50)
    with open(file_path + ".txt", 'w', encoding='utf-8') as f:
        f.write(text)

    for d in data:
        if d.startswith('Name'):
            print(d)
            names.append(d)

        elif d.startswith('Fat') or d.startswith('Hus'):
            print(d)
            fhn = d
            print(data[data.index(d) + 2])
            if not data[data.index(d) + 2].startswith('Hou'):
                fhn = d + " " + data[data.index(d) + 2]
            fh.append(fhn + "====" + str(data.index(d)))
        elif d.startswith('Hou'):
            pass

# In[26]:


print(names)

# In[36]:


print(fh)

# In[37]:


len(names), len(fh)

# In[ ]:




