import cv2
import base64

def base64Con(img):
    img = cv2.imread(img)
    jpg_img = cv2.imencode('.jpg', img)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    # print(b64_string)
    return b64_string