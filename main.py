from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

import cv2
import pytesseract
# im2=''
#
from PIL import Image
# for i in range(6,41):


# importing module
from pymongo import MongoClient

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client['pytesseract']

# Access collection of the database
mycollection = mydatabase['test1']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

name = []
gardian = []
age = []
address = []
Voter = []


# converting a non-readable text to data ,  inserting the data to the database
# mydatabase.myTable.deletemany({})
def covert(x, y, w, h, im2):
    try:
        lis = []
        f = open('test.txt', 'w')
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        # file = open("recognized.txt", "a")
        text = pytesseract.image_to_string(cropped)
        f.write(text)
        f.close()
        f = open('test.txt', 'r')
        read_lines = f.readlines()
        for i in read_lines:
            print(i)
            # global Voter_id
            if len(i) == 12:
                Voter_id = i.rstrip()
                # print(len(Voter_id))
                if len(Voter_id) == 11:
                    if Voter_id.isalpha() == False:
                        Voter.append(Voter_id)

            elif len(i) == 11:
                Voter_id = i.rstrip()
                # print(len(Voter_id))
                if len(Voter_id) == 11:
                    if Voter_id.isalpha() == False:
                        Voter_id = Voter_id
                        Voter.append(Voter_id)
            else:

                if i.startswith('Photo') or i.startswith('Ava'):
                    pass
                elif i != "\n":
                    if i not in lis:
                        result = lis.append(i)
        if len(lis) == 5:
            gardian = lis[1] + lis[2]
            lis[1] = gardian
            lis.remove(lis[2])
        # print(lis)
        elif len(lis) == 6:
            # print(lis)
            pass
        # for i in lis:
        #     if i.startswith('Name'):
        #         nm=i
        #     elif i.startswith('Age'):
        #         Age=i
        #
        #     elif i.startswith('House'):
        #         adr=i
        #     elif i.startswith()
        #         gar=i
        print(lis)

        rec = mydatabase.myTable.insert({'Voter_id': Voter_id,
                                         'details': lis})
    except:
        rec = mydatabase.myTable.insert({'Voter_id': 'null',
                                         'details': lis})


def ima(x, y, w, h, im2):
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 3)
    img = cv2.resize(rect, (750, 1300))
    cv2.imshow('d', img)
    covert(x, y, w, h, im2)
    cv2.waitKey(3)


# for i in lis:
#     if i.startswith('Name'):
#         nm=i
#     elif i.startswith('Age'):
#         Age=i
#
#     elif i.startswith('House'):
#         adr=i
#     elif i.startswith()
#         gar=i


# ima(170, 250,1220,430)
# ima(1390, 250,1220,430 )
# ima(2620, 250,1220,430)
# ima(2620, 250+430,1220,430)


def convertion(path):
    image = Image.open(path)
    image = image.resize((4000, 5000), Image.ANTIALIAS)
    # image.show(0)
    image.save(fp="newimage.png")
    img = cv2.imread('newimage.png')
    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    c = 0
    de = 250
    for i in range(10):
        ima(170, de, 1220, 430, im2)
        ima(1390, de, 1220, 430, im2)
        ima(2610, de, 1220, 430, im2)
        c = c + 1
        print(c)
        de = de + 420


import os

folder = 'D:\downloads\pdf'
l = os.listdir(folder)
le = len(l)
print(le)
for i in range(le):
    p = f'{folder}\{l[i]}'
    convertion(p)
    print(p, 'is done')

import numpy as np

img = cv2.imread()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,50,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
print("Number of contours detected:", len(contours))

for cnt in contours:
   x1,y1 = cnt[0][0]
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   if len(approx) == 4:
      x, y, w, h = cv2.boundingRect(cnt)
      ratio = float(w)/h
      if ratio >= 0.9 and ratio <= 1.1:
          pass
         # img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
         # cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
      else:
         cv2.putText(img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()