import cv2
import numpy as np
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r"C:\Users\anves\PycharmProjects\pythonProject\out30.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,50,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
print("Number of contours detected:", len(contours))
c=1
directory = r'C:\Users\anves\PycharmProjects\pythonProject\cropped'
def covert(x, y, w, h, im2):

        lis = []
        f = open('test.txt', 'a')
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        cv2.imshow('show',cropped)
        os.chdir(directory)

        # List files and directories
        # in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
        print("Before saving image:")
        print(os.listdir(directory))

        # Filename
        filename = 'savedImage1.jpg'

        # Using cv2.imwrite() method
        # Saving the image
        cv2.imwrite(filename, img)

        # List files and directories
        # in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'
        print("After saving image:")
        print(os.listdir(r'C:\Users\anves\PycharmProjects\pythonProject\cropped'))

        print('Successfully saved')
        img_path = f'{directory}\{filename}'
        saved_img = cv2.imread(img_path)
        file = open("recognized.txt", "a")
        text = pytesseract.image_to_string(saved_img)
        text=''
        # cv2.waitKey(0)
        f.write(text)
        f.close()

        # f = open('test.txt', 'r')
        # read_lines = f.readlines()
        # for i in read_lines:
        #     print(i)






def ima(x, y, w, h, im2):
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 3)
    img = cv2.resize(rect, (750, 1300))
    # cv2.imshow('d', img)
    covert(x, y, w, h, im2)
    # cv2.waitKey(3)




area = []
value =[]

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
        # imx = cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        area.append((h*w))
        value.append((h,w,x,y))

        # ima(img, [cnt])
        # covert(im2=img,cnt=[cnt])
        # print([cnt],'-----------------',c)
        # print(type([cnt]))
        # print(cv2.minAreaRect([cnt]))
        c=c+1
        if c==100:
            pass
         # print([cnt], '-----------------', c)
         # print(type([cnt]))


print((area))
print((value))
for i in range(len(area)):
    if area[i]>16000:
        xa =value[i][2]
        ya=value[i][3]
        l =value[i][0]
        w =value[i][1]
        # cv2.rectangle(img, (xa, ya), (xa + w, ya + l), (0, 255, 0), 2)
        ima(x=xa,y=ya,w=w,h=l,im2=img)




# x= cv2.imshow("Shapes", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()