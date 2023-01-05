import base64

img_file = open('/home/madhu/Documents/django_crud/img220325/download.jpg', "rb")
data = base64.b64encode(img_file.read())
print(data)