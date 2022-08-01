import base64
import pyqrcode
from rest_framework import serializers
from .models import barmodel,barreaddb
from barcode_generator.bar import logic

class barserializer(serializers.ModelSerializer):
    class Meta:
        model = barmodel
        fields = 'product_name','product_code' ,'pack_code'

    def create(self, validated_data):
        product_name = validated_data['product_name']
        product_code = validated_data['product_code']
        pack_code = validated_data['pack_code']
        a = product_code + " " + pack_code
        b = pyqrcode.create(a)
        combined = b.png(f'{product_name}.png', scale=6)
        with open('myqr.png', 'rb') as img:
            encoded = base64.b64encode(img.read())
            print(encoded)
            user = barmodel.objects.create(product_name=product_name, product_code=product_code, pack_code=pack_code,bar_code=encoded)
            user.save()
            return user





class retrieveserializer(serializers.ModelSerializer):
    class Meta:
        model = barreaddb
        fields = '__all__'

